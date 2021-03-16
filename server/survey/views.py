from flask import Blueprint,render_template,redirect,url_for,request, jsonify, flash
from server import db
from sqlalchemy import distinct, inspect


from server.models import Cement_and_manufacturing, Electricity, Natural_gas, Otis_transportation, Waste, Aviation, Zip_pop, Zip_data, Solutions
from server.survey.forms import RecForm
from server.emissions.views import object_as_dict, coalesce
import collections


survey_blueprint = Blueprint('survey', __name__, template_folder='../templates')


# Actions
@survey_blueprint.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    form = RecForm()
    tableData = []
    columnNames = ["ID", "Sector", "HIP", "Recommendation", "GHG Reduction Potential"]
    if request.method == 'POST':
        if form.allSol.data & form.allSec.data:
            query = Solutions.query.all()
            # query = session.query.with_entities(Solutions.recommendations_id, Solutions.section, Solutions.subsection, Solutions.solution_description, Solutions.ghg_reduction_potential).all()
        elif form.allSol.data == False:
            if form.allSec.data == True:
                query = Solutions.query.filter((Solutions.equity & form.equity.data) | \
                (Solutions.economic_sustainability & form.econSus.data) | \
                (Solutions.local_environmental_quality & form.envQuality.data) | \
                (Solutions.enhances_public_safety & form.healthSafety.data) | \
                (Solutions.builds_resilience & form.resilience.data))
            elif form.allSec.data == False:
                if form.transportation.data == True:
                    if form.energy.data == False: 
                        if form.waste.data == False:
                            query = Solutions.query.filter(((Solutions.equity & form.equity.data) | \
                            (Solutions.economic_sustainability & form.econSus.data) | \
                            (Solutions.local_environmental_quality & form.envQuality.data) | \
                            (Solutions.enhances_public_safety & form.healthSafety.data) | \
                            (Solutions.builds_resilience & form.resilience.data)) & (Solutions.vech_tran))
                if form.transportation.data == True:
                    if form.energy.data == True:
                        if form.waste.data == False:
                            query = Solutions.query.filter(((Solutions.equity & form.equity.data) | \
                            (Solutions.economic_sustainability & form.econSus.data) | \
                            (Solutions.local_environmental_quality & form.envQuality.data) | \
                            (Solutions.enhances_public_safety & form.healthSafety.data) | \
                            (Solutions.builds_resilience & form.resilience.data)) & ((Solutions.vech_tran) | (Solutions.energy)))
                if form.transportation.data == True:
                    if form.energy.data == False:
                        if form.waste.data == True:
                            query = Solutions.query.filter(((Solutions.equity & form.equity.data) | \
                            (Solutions.economic_sustainability & form.econSus.data) | \
                            (Solutions.local_environmental_quality & form.envQuality.data) | \
                            (Solutions.enhances_public_safety & form.healthSafety.data) | \
                            (Solutions.builds_resilience & form.resilience.data)) & ((Solutions.vech_tran) | (Solutions.waste)))
                if form.transportation.data == False:
                    if form.energy.data == True:
                        if form.waste.data == False:
                            query = Solutions.query.filter(((Solutions.equity & form.equity.data) | \
                            (Solutions.economic_sustainability & form.econSus.data) | \
                            (Solutions.local_environmental_quality & form.envQuality.data) | \
                            (Solutions.enhances_public_safety & form.healthSafety.data) | \
                            (Solutions.builds_resilience & form.resilience.data)) & (Solutions.energy))
                if form.transportation.data == False:
                    if form.energy.data == True:
                        if form.waste.data == True:
                            query = Solutions.query.filter(((Solutions.equity & form.equity.data) | \
                            (Solutions.economic_sustainability & form.econSus.data) | \
                            (Solutions.local_environmental_quality & form.envQuality.data) | \
                            (Solutions.enhances_public_safety & form.healthSafety.data) | \
                            (Solutions.builds_resilience & form.resilience.data)) & ((Solutions.energy) | (Solutions.waste)))
                if form.transportation.data == False:
                    if form.energy.data == False:
                        if form.waste.data == True:
                            query = Solutions.query.filter(((Solutions.equity & form.equity.data) | \
                            (Solutions.economic_sustainability & form.econSus.data) | \
                            (Solutions.local_environmental_quality & form.envQuality.data) | \
                            (Solutions.enhances_public_safety & form.healthSafety.data) | \
                            (Solutions.builds_resilience & form.resilience.data)) & (Solutions.waste))
        else:
            if form.allSol.data == True:
                query = Solutions.query.filter((Solutions.vech_tran & form.transportation.data) | \
                (Solutions.energy & form.energy.data) | \
                (Solutions.waste & form.waste.data))
        # columnNames = Solutions.__tablename__.columns.keys()
        for row in query:
            d = object_as_dict(row)
            tableData.append(d.values())

    return render_template('/mainPages/recommendations.html', form=form, columnNames=columnNames, tableData=tableData)