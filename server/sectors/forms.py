from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class CityCountyZipDropDown(FlaskForm):
    county = SelectField('county', choices=[])
    city = SelectField('city', choices=[])
    zip = SelectField('zip', choices=[])
    submit = SubmitField('Get Data')
