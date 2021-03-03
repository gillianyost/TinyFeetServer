from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class CityCountyZipDropDown(FlaskForm):
    county = SelectField('County')
    city = SelectField('City')
    zip = SelectField('Zip')
    countySubmit = SubmitField('Get Data By County')
    citySubmit = SubmitField('Get Data By City')
    zipSubmit = SubmitField('Get Data By Zip')


