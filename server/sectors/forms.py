from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class CityCountyZipDropDown(FlaskForm):
    county = SelectField('County')
    city = SelectField('City')
    zip = SelectField('Zip')
    countySubmit = SubmitField('Get Data By County')
    citySubmit = SubmitField('Get Data By City')
    zipSubmit = SubmitField('Get Data By Zip')

class tableSelectForm(FlaskForm):
    submit = SubmitField('Get Table Data')
    tables = SelectField('', choices=[ "Select A Table To Read",
                                        'cement_and_manufacturing',
                                        'waste',
                                        'electricity',
                                        'natural_gas',
                                        'aviation',
                                        'zip_pop'
                                        ])



