from flask import Blueprint,render_template,redirect,url_for,request, jsonify, flash
from server import db
from sqlalchemy import distinct, inspect, and_, or_, desc


from server.models import Cement_and_manufacturing, Electricity, Natural_gas, Otis_transportation, Waste, Aviation, Zip_pop, Zip_data, Solutions
from server.survey.forms import RecForm
from server.emissions.views import object_as_dict, coalesce
import collections

survey_blueprint = Blueprint('survey', __name__, template_folder='../templates')


# Actions
@survey_blueprint.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    form = RecForm()

    if request.method == 'POST':
        # Initialize
        tableData = []
        columnNames = []
        equity = econSus = envQuality = healthSafety = resilience =  0
        waste = energy = vech_tran = allSol = allSec = None
        
        # Grab boolean form data
        if form.allSol.data:
            allSol = 1
        if form.equity.data:
            equity = 1
        if form.econSus.data:
            econSus = 1
        if form.envQuality.data:
            envQuality = 1
        if form.healthSafety.data:
            healthSafety = 1
        if form.resilience.data:
            resilience = 1

        if form.allSec.data:
            allSec = 1
        if form.transportation.data:
            vech_tran = 1
        if form.energy.data:
            energy = 1
        if form.waste.data:
            waste = 1

        # Error Checking for no input
        if equity == 0 and econSus == 0 and envQuality == 0 and healthSafety == 0 and resilience == 0 and allSol == None:
            flash("Please Select a Solution Type")
            return render_template('/mainPages/recommendations.html', form=form)

        if vech_tran == 0 and energy == 0 and waste == 0 and allSec == None:
            flash("Please Select an Emissions Sector")
            return redirect('/recommendations')


        # All solutions / all sector cases
        if form.allSol.data and form.allSec.data:
            query = db.session.query(Solutions).order_by(desc('ghg_reduction_potential'))

        elif form.allSol.data:
            query = db.session.query(Solutions).filter(or_(
                        Solutions.vech_tran==vech_tran,
                        Solutions.energy==energy,
                        Solutions.waste==waste
                        )).order_by(desc('ghg_reduction_potential'))

        elif form.allSec.data:
            query = db.session.query(Solutions).filter(and_(
                        Solutions.equity==equity,
                        Solutions.economic_sustainability==econSus,
                        Solutions.local_environmental_quality==envQuality,
                        Solutions.enhances_public_safety==healthSafety,
                        Solutions.builds_resilience==resilience,
                        )).order_by(desc('ghg_reduction_potential'))



        # Specific solution/solutions and sector/sectors case
        # Combination of solutions inputs are AND case, combination of sector inputs are OR case
        else:
            query = db.session.query(Solutions).filter(and_(
                        Solutions.equity==equity,
                        Solutions.economic_sustainability==econSus,
                        Solutions.local_environmental_quality==envQuality,
                        Solutions.enhances_public_safety==healthSafety,
                        Solutions.builds_resilience==resilience,
                        )).filter(or_(                        
                        Solutions.vech_tran==vech_tran,
                        Solutions.energy==energy,
                        Solutions.waste==waste
                        )).order_by(desc('ghg_reduction_potential'))
        
        
        # Error check no results from query
        if query.count() == 0:
            flash("No recommendations for that combination of filter settings")
            return redirect('/recommendations')
    

        # Data is just a dictionary after conversion so can be manipulated using basic dictionary comprehension
        # You can comment out the pop functions to help debug
        for row in query:
            d = object_as_dict(row)
            d.pop('recommendations_id')
            d.pop('equity')
            d.pop('economic_sustainability')
            d.pop('local_environmental_quality')
            d.pop('enhances_public_safety')
            d.pop('builds_resilience')
            d.pop('vech_tran')
            d.pop('energy')
            d.pop('waste')

            # These columns are probably unneccesary.  We should also think about displaying the data in a way other than a table
            # Like maybe a card with a picture or something
            # d.pop('section')
            # d.pop('subsection')
            # d.pop('ghg_reduction_potential')

            tableData.append(d.values())

        # Column names are the dict keys
        columnNames = [column.replace("_", " ").capitalize() for column in d.keys()]

        # This is the POST return
        return render_template('/mainPages/recommendations.html', form=form, columnNames=columnNames, tableData=tableData)
    # Fall-through GET request case return
    return render_template('/mainPages/recommendations.html', form=form)