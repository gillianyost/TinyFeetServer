from flask import Blueprint,render_template,redirect,url_for,request, jsonify, flash
from server import db
from sqlalchemy import distinct, inspect
import collections

from server.models import Cement_and_manufacturing, Electricity, Natural_gas, Otis_transportation, Waste, Aviation, Zip_pop, Zip_data, Solutions
from server.survey.forms import RecForm
from server.sectors.views import object_as_dict
import collections


survey_blueprint = Blueprint('survey', __name__, template_folder='../templates')


# Actions
@survey_blueprint.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    form = RecForm()
    columnNames = []
    tableData = []
    if request.method == 'POST':
        columnNames = Solutions.__table__.columns.keys()
       
        if form.allSol.data:
            # query = Solutions.query(Solutions.solution_description, \
            # Solutions.section, \
            # Solutions.subsection, \
            # Solutions.ghg_reduction_potential) # Cannot get to work TO DO

            # columnNames = Solutions.__tablename__.columns.keys()  # Cannot get to work TO DO
            query = Solutions.query.all()
        else: 
            # query = Solutions.query(Solutions.solution_description, \
            # Solutions.section, \
            # Solutions.subsection, \
            # Solutions.ghg_reduction_potential)\
            # .filter((Solutions.equity & form.equity.data) | \
            # (Solutions.economic_sustainability & form.econSus.data) | \
            # (Solutions.local_environmental_quality & form.envQuality.data) | \
            # (Solutions.enhances_public_safety & form.healthSafety.data) | \
            # (Solutions.builds_resilience & form.resilience.data)) # Cannot get to work TO DO

            # columnNames = Solutions.__tablename__.columns.keys()  # Cannot get to work TO DO
            query = Solutions.query.filter((Solutions.equity & form.equity.data) | \
            (Solutions.economic_sustainability & form.econSus.data) | \
            (Solutions.local_environmental_quality & form.envQuality.data) | \
            (Solutions.enhances_public_safety & form.healthSafety.data) | \
            (Solutions.builds_resilience & form.resilience.data))

        for row in query:
            d = object_as_dict(row)
            tableData.append(d.values())
    
    # if request.method == 'POST':
    #     if form.equity.data:
    #         columnNames = recommendations.__table__.columns.keys()
    #         query = recommendations.all()
    
    # tableData = []
    # d = object_as_dict(row)
    # tableData.append(d.values())

    return render_template('/mainPages/recommendations.html', form=form, columnNames=columnNames, tableData=tableData)