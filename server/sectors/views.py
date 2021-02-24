from flask import Blueprint,render_template,redirect,url_for,request, jsonify
from server import db
from server.sectors.forms import CityCountyZipDropDown
from server.models import cement_and_manufacturing, electricity, natural_gas, otis_transportation, waste, aviation, zip_pop, Zip_data
from sqlalchemy import distinct

sectors_blueprint = Blueprint('sectors', __name__, template_folder='../templates')

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
    return render_template('read.html', 
        Cement_And_Manufacturing=Cement_And_Manufacturing, 
        Electricity=Electricity,
        Natural_gas=Natural_gas,
        OTIS_Transportation=OTIS_Transportation,
        Waste=Waste,
        Aviation=Aviation,
        Zip_pop=Zip_pop
        )


# ------- Select page default and submit button handling to load table ------- #
@sectors_blueprint.route('/select', methods=['GET', 'POST'])
def select():
    form = CityCountyZipDropDown()
    form.county.choices = [(row.county) for row in db.session.query(zip_pop.county).distinct(zip_pop.county).order_by(zip_pop.county)]
    
    if request.method == 'POST':
        # Change back dropdown options after they reset on page reload
        city = form.county.data
        zip = form.city.data
        form.city.choices = [(row.city) for row in db.session.query(zip_pop.city).filter_by(county=form.county.data).distinct(zip_pop.county).order_by(zip_pop.city)]
        form.zip.choices = [(row.zip) for row in db.session.query(zip_pop.zip).filter_by(city=form.city.data).all()]

        # Query model
        zip_data = Zip_data.query.filter_by(zip=form.zip.data)

        return render_template('select.html', form=form, zip_data=zip_data)
    return render_template('select.html', form=form)


# --------------------- Dynamic Dropdown Option Changing for Select page--------------------- #
@sectors_blueprint.route('/<county>')
def city(county):
    rows = db.session.query(zip_pop.city).filter_by(county=county).distinct(zip_pop.county).order_by(zip_pop.city)
    cityArray = []
    for row in rows:
        cityObj = {}
        cityObj['name'] = row.city
        cityArray.append(cityObj)
    return jsonify({'cities' : cityArray})


@sectors_blueprint.route('/<county>/<city>')
def zip(county, city):
    rows = db.session.query(zip_pop.zip).filter_by(city=city).all()
    zipArray = []
    for row in rows:
        zipObj = {}
        zipObj['zip'] = row.zip
        zipArray.append(zipObj)
    return jsonify({'zip_codes' : zipArray})

