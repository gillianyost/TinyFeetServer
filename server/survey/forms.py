from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, BooleanField


class RecForm(FlaskForm):
    equity = BooleanField('Equity')
    envQuality = BooleanField('Local Environmental Quality')
    healthSafety = BooleanField('Enhancing Public Health and Safety')
    resilience = BooleanField('Building Community Resilience')

    cementMan = BooleanField('Cement And Manufacturing')
    waste = BooleanField('Waste')
    electricity = BooleanField('Electricity')
    naturalGas = BooleanField('Natural Gas')
    transportation = BooleanField('Transportation')

    submit = SubmitField()
