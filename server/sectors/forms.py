from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class CityCountyZipDropDown(FlaskForm):
    county = SelectField('County', choices=[])
    city = SelectField('City', choices=[])
    zip = SelectField('Zip', choices=[])
    submit = SubmitField('Get Data')

