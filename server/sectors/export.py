import os
from server import db
import pandas as pd
from flask import Blueprint, render_template, request, jsonify, make_response
import flask_excel as excel

from server.models import cement_and_manufacturing, electricity, natural_gas, otis_transportation, waste, aviation, zip_pop, Zip_data


export_blueprint = Blueprint('export', __name__, template_folder='../templates')

@export_blueprint.route('/export/<tableName>')
def export(tableName):
    query_sets = tableName.query.all()
    col_names = db.session.__table__.columns.keys()
    return excel.make_response_from_query_sets(query_sets, col_names, "xls")