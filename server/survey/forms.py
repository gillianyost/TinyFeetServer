from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, BooleanField


class RecForm(FlaskForm):
    allSol = BooleanField('All Recommendations', default=True)
    equity = BooleanField('Equity')
    econSus = BooleanField('Economic Sustainability')
    envQuality = BooleanField('Local Environmental Quality')
    healthSafety = BooleanField('Enhancing Public Health and Safety')
    resilience = BooleanField('Building Community Resilience')

    allSec = BooleanField('All Sectors', default=True)
    cementMan = BooleanField('Cement And Manufacturing')
    waste = BooleanField('Waste and Land Management')
    electricity = BooleanField('Electricity')
    energy = BooleanField('Energy')
    naturalGas = BooleanField('Natural Gas')
    transportation = BooleanField('Vechicles and Transportation')

    submit = SubmitField()
