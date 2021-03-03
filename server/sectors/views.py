from flask import Blueprint,render_template,redirect,url_for,request, jsonify, flash
from server import db
from server.sectors.forms import CityCountyZipDropDown
from server.models import cement_and_manufacturing, electricity, natural_gas, otis_transportation, waste, aviation, zip_pop, Zip_data
from sqlalchemy import distinct, inspect
import collections, functools, operator 

sectors_blueprint = Blueprint('sectors', __name__, template_folder='../templates')


# ----------------------------- Helper Functions ----------------------------- #

# This function replaces Null or 'None' values with 0 to play nice with google charts
def coalesce(*arg): return next((a for a in arg if a is not None), 0)

# This function converts query result to dict
def object_as_dict(obj):
    return {c.key: coalesce(getattr(obj, c.key))
        for c in inspect(obj).mapper.column_attrs}

# ------------------------------ Read page route ----------------------------- #

@sectors_blueprint.route('/read')
def read():
    Cement_And_Manufacturing = cement_and_manufacturing.query.all()
    Electricity = electricity.query.all()
    Natural_gas = natural_gas.query.all()
    OTIS_Transportation = otis_transportation.query.all()
    Waste = waste.query.all()
    Aviation = aviation.query.all()
    Zip_pop = zip_pop.query.all()
    return render_template('/mainPages/read.html', 
        Cement_And_Manufacturing=Cement_And_Manufacturing, 
        Electricity=Electricity,
        Natural_gas=Natural_gas,
        OTIS_Transportation=OTIS_Transportation,
        Waste=Waste,
        Aviation=Aviation,
        Zip_pop=Zip_pop
        )


# ------- Select page GET route and POST form handling to load table chart ------- #

@sectors_blueprint.route('/select', methods=['GET', 'POST'])
def select():
    form = CityCountyZipDropDown()
    county = form.county.data
    city = form.city.data
    zip = form.zip.data
    
    if request.method == 'POST':
        if form.countySubmit.data:
            if county == "Select Option":
                flash("Please Select a County Option")
            else:
                return redirect(f'select/county/{county}')
        elif form.citySubmit.data:
            if city == "Select Option":
                flash("Please Select a City Option")
            else:
                return redirect(f'select/city/{city}')
        elif form.zipSubmit.data:
            if zip == "Select Option":
                flash("Please Select a Zip Option")
            else:
                return redirect(f'select/zip/{zip}')
        else:
            zip = request.form.get('zipInput')
            if (db.session.query(Zip_data).filter_by(zip=zip)).count() == 0:
                flash("Please Enter a Valid Zip Code")
            else:
                return redirect(f'select/zip/{zip}')
        return redirect(f'/sectors/select')
    
    if request.method == 'GET':
        form.county.choices = ["Select Option"] + [(row.county) for row in db.session.query(zip_pop.county).distinct(zip_pop.county).order_by(zip_pop.county)]
        form.city.choices = ["Select Option"] + [(row.city) for row in db.session.query(zip_pop.city).distinct(zip_pop.city).order_by(zip_pop.city)]
        form.zip.choices = ["Select Option"] + [(row.zip) for row in db.session.query(zip_pop.zip).distinct(zip_pop.zip).order_by(zip_pop.zip)]

    return render_template('mainPages/select.html', form=form)


# -------------------------- Generate Chart From Zip ------------------------- #

@sectors_blueprint.route('/select/zip/<zip>')
def chartZip(zip):
    form = CityCountyZipDropDown()
    query = db.session.query(Zip_data).filter_by(zip=zip)
    
    for row in query:
        data = (object_as_dict(row))

    # Remove zip and pop non-numerical data points
    data.pop('zip')
    city = data.pop('city')
    county = data.pop('county')
    # Must remove aviation data point for now because google charts does not like decimal data type
    aviation = data.pop('aviation')
    # Convert to list of lists and add labels
    zipData = list(map(list, data.items()))
    zipData.insert(0, ['Sector', 'Emissions'])

    form.county.choices = [(row.county) for row in db.session.query(zip_pop.county).distinct(zip_pop.county).order_by(zip_pop.county)]
    form.city.choices = [(row.city) for row in db.session.query(zip_pop.city).filter_by(county=county).distinct(zip_pop.county).order_by(zip_pop.city)]
    form.zip.choices = [(row.zip) for row in db.session.query(zip_pop.zip).filter_by(city=city).all()]
    form.zip.data = zip
    form.city.data = city
    form.county.data = county

    return render_template('mainPages/select.html', form=form, zipData=zipData, area=zip)


# -------------------------- Generate Chart From City ------------------------- #

@sectors_blueprint.route('/select/city/<city>')
def chartCity(city):
    form = CityCountyZipDropDown()

    query = db.session.query(Zip_data).filter_by(city=city)
    if query.count() == 0:
        flash("That City Does Not Exist!")
        return render_template('mainPages/select.html', form=form,)

    else:
        rows = []
        for row in query:
            d = object_as_dict(row)
            d.pop('zip')
            city = d.pop('city')
            county = d.pop('county')
            # Must remove aviation data point for now because google charts does not like decimal data type
            d.pop('aviation')
            rows.append(d)
        
        # sum the values with same keys 
        counter = collections.Counter() 
        for d in rows:  
            counter.update(d)
        data = dict(counter) 

        # Convert to list of lists and add labels
        zipData = list(map(list, data.items()))
        zipData.insert(0, ['Sector', 'Emissions'])

        form.county.choices = [(row.county) for row in db.session.query(zip_pop.county).distinct(zip_pop.county).order_by(zip_pop.county)]
        form.city.choices = [(row.city) for row in db.session.query(zip_pop.city).filter_by(county=county).distinct(zip_pop.county).order_by(zip_pop.city)]
        form.zip.choices = ["Select Option"] + [(row.zip) for row in db.session.query(zip_pop.zip).filter_by(city=city).all()]
        form.zip.data = ["Select Option"]
        form.city.data = city
        form.county.data = county

        return render_template('mainPages/select.html', form=form, zipData=zipData, area=city)


# -------------------------- Generate Chart From County ------------------------- #

@sectors_blueprint.route('/select/county/<county>')
def chartCounty(county):
    form = CityCountyZipDropDown()
    query = db.session.query(Zip_data).filter_by(county=county)

    if query.count() == 0:
        flash("That Zip Code Does Not Exist!")
        return render_template('mainPages/select.html', form=form,)

    else:
        rows = []
        for row in query:
            d = object_as_dict(row)
            d.pop('zip')
            city = d.pop('city')
            county = d.pop('county')
            # Must remove aviation data point for now because google charts does not like decimal data type
            d.pop('aviation')
            rows.append(d)
        
        # sum the values with same keys 
        counter = collections.Counter() 
        for d in rows:  
            counter.update(d)
        data = dict(counter) 

        # Convert to list of lists and add labels
        zipData = list(map(list, data.items()))
        zipData.insert(0, ['Sector', 'Emissions'])

        form.county.choices = [(row.county) for row in db.session.query(zip_pop.county).distinct(zip_pop.county).order_by(zip_pop.county)]
        form.city.choices = ["Select Option"] + [(row.city) for row in db.session.query(zip_pop.city).filter_by(county=county).distinct(zip_pop.county).order_by(zip_pop.city)]
        form.zip.choices = ["Select Option"] + [(row.zip) for row in db.session.query(zip_pop.zip).filter_by(city=city).all()]
        form.zip.data = ["Select Option"]
        form.city.data = ["Select Option"]
        form.county.data = county

        return render_template('mainPages/select.html', form=form, zipData=zipData, area=county)


# --------------------- Dynamic Dropdown Option Changing for Select page--------------------- #

@sectors_blueprint.route('/<county>')
def city(county):
    rows = db.session.query(zip_pop.city).filter_by(county=county).distinct(zip_pop.county).order_by(zip_pop.city)
    cityArray = []
    for row in rows:
        cityObj = {}
        cityObj['option'] = row.city
        cityArray.append(cityObj)
    return jsonify({'cities' : cityArray})


@sectors_blueprint.route('/<county>/<city>')
def zip(county, city):
    rows = db.session.query(zip_pop.zip).filter_by(city=city).all()
    zipArray = []
    for row in rows:
        zipObj = {}
        zipObj['option'] = row.zip
        zipArray.append(zipObj)
    return jsonify({'zip_codes' : zipArray})

