from flask import Blueprint,render_template,redirect,url_for,request, jsonify, flash
from server import db
from sqlalchemy import distinct, inspect
import collections

from server.models import Cement_and_manufacturing, Electricity, Natural_gas, Otis_transportation, Waste, Aviation, Zip_pop, Zip_data, Solutions, Solutions_vech_tran, Solutions_waste, Solutions_vech_tran_energy, Solutions_energy, Solutions_energy_waste, Solutions_waste_vech_tran
from server.survey.forms import RecForm
from server.emissions.views import object_as_dict, coalesce
import collections


survey_blueprint = Blueprint('survey', __name__, template_folder='../templates')


# Actions
@survey_blueprint.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    form = RecForm()
    columnNames = []
    tableData = []
    if request.method == 'POST':
       
        if form.allSol.data & form.allSec.data:
            query = Solutions.query.all()
            #columnNames = Solutions.__tablename__.columns.keys()
            for row in query:
                d = object_as_dict(row)
                tableData.append(d.values())

        elif form.allSol.data == False:
            if form.allSec.data == True:
                query = Solutions.query.filter((Solutions.equity & form.equity.data) | \
                (Solutions.economic_sustainability & form.econSus.data) | \
                (Solutions.local_environmental_quality & form.envQuality.data) | \
                (Solutions.enhances_public_safety & form.healthSafety.data) | \
                (Solutions.builds_resilience & form.resilience.data))
                #columnNames = Solutions.__tablename__.columns.keys()
                for row in query:
                    d = object_as_dict(row)
                    tableData.append(d.values())
            elif form.allSec.data == False:
                if form.transportation.data == True:
                    if form.energy.data == False: 
                        if form.waste.data == False:
                            query = Solutions_vech_tran.query.filter((Solutions_vech_tran.equity & form.equity.data) | \
                            (Solutions_vech_tran.economic_sustainability & form.econSus.data) | \
                            (Solutions_vech_tran.local_environmental_quality & form.envQuality.data) | \
                            (Solutions_vech_tran.enhances_public_safety & form.healthSafety.data) | \
                            (Solutions_vech_tran.builds_resilience & form.resilience.data))
                if form.transportation.data == True:
                    if form.energy.data == True:
                        if form.waste.data == False:
                            query = Solutions_vech_tran_energy.query.filter((Solutions_vech_tran_energy.equity & form.equity.data) | \
                            (Solutions_vech_tran_energy.economic_sustainability & form.econSus.data) | \
                            (Solutions_vech_tran_energy.local_environmental_quality & form.envQuality.data) | \
                            (Solutions_vech_tran_energy.enhances_public_safety & form.healthSafety.data) | \
                            (Solutions_vech_tran_energy.builds_resilience & form.resilience.data))
                if form.transportation.data == True:
                    if form.energy.data == False:
                        if form.waste.data == True:
                            query = Solutions_waste_vech_tran.query.filter((Solutions_waste_vech_tran.equity & form.equity.data) | \
                            (Solutions_waste_vech_tran.economic_sustainability & form.econSus.data) | \
                            (Solutions_waste_vech_tran.local_environmental_quality & form.envQuality.data) | \
                            (Solutions_waste_vech_tran.enhances_public_safety & form.healthSafety.data) | \
                            (Solutions_waste_vech_tran.builds_resilience & form.resilience.data))
                if form.transportation.data == False:
                    if form.energy.data == True:
                        if form.waste.data == False:
                            query = Solutions_energy.query.filter((Solutions_energy.equity & form.equity.data) | \
                            (Solutions_energy.economic_sustainability & form.econSus.data) | \
                            (Solutions_energy.local_environmental_quality & form.envQuality.data) | \
                            (Solutions_energy.enhances_public_safety & form.healthSafety.data) | \
                            (Solutions_energy.builds_resilience & form.resilience.data))
                if form.transportation.data == False:
                    if form.energy.data == True:
                        if form.waste.data == True:
                            query = Solutions_energy_waste.query.filter((Solutions_energy_waste.equity & form.equity.data) | \
                            (Solutions_energy_waste.economic_sustainability & form.econSus.data) | \
                            (Solutions_energy_waste.local_environmental_quality & form.envQuality.data) | \
                            (Solutions_energy_waste.enhances_public_safety & form.healthSafety.data) | \
                            (Solutions_energy_waste.builds_resilience & form.resilience.data))
                if form.transportation.data == False:
                    if form.energy.data == False:
                        if form.waste.data == True:
                            query = Solutions_waste.query.filter((Solutions_waste.equity & form.equity.data) | \
                            (Solutions_waste.economic_sustainability & form.econSus.data) | \
                            (Solutions_waste.local_environmental_quality & form.envQuality.data) | \
                            (Solutions_waste.enhances_public_safety & form.healthSafety.data) | \
                            (Solutions_waste.builds_resilience & form.resilience.data))
                #columnNames = Solutions.__tablename__.columns.keys()
                for row in query:
                    d = object_as_dict(row)
                    tableData.append(d.values())
        elif form.allSec.data == False:
            if form.allSol.data == True:
                query = Solutions.query.filter((Solutions.vech_tran & form.transportation.data) | \
                (Solutions.energy & form.energy.data) | \
                (Solutions.waste & form.waste.data))
                #columnNames = Solutions.__tablename__.columns.keys()
                for row in query:
                    d = object_as_dict(row)
                    tableData.append(d.values())

    return render_template('/mainPages/recommendations.html', form=form, columnNames=columnNames, tableData=tableData)