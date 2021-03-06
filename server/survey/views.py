from flask import Blueprint,render_template,redirect,url_for,request, jsonify, flash
from server import db
from server.models import Cement_and_manufacturing, Electricity, Natural_gas, Otis_transportation, Waste, Aviation, Zip_pop, Zip_data, Solutions
from sqlalchemy import distinct, inspect
import collections


survey_blueprint = Blueprint('survey', __name__, template_folder='../templates')


@survey_blueprint.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    form = RecForm()
    
    return render_template('/mainPages/recommendations.html', form=form)