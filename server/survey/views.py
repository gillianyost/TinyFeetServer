from flask import Blueprint,render_template,redirect,url_for,request, jsonify, flash
from server import db
from server.models import cement_and_manufacturing, electricity, natural_gas, otis_transportation, waste, aviation, zip_pop, Zip_data
from sqlalchemy import distinct, inspect
import collections


survey_blueprint = Blueprint('survey', __name__, template_folder='../templates')

def object_as_dict(obj):
    return {c.key: coalesce(getattr(obj, c.key))
        for c in inspect(obj).mapper.column_attrs}

@survey_blueprint.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    form = RecForm()
    
    return render_template('/mainPages/recommendations.html', form=form)