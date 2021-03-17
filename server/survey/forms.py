from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, BooleanField


class RecForm(FlaskForm):
    allSol = BooleanField('All Recommendations')
    equity = BooleanField('Equity')
    econSus = BooleanField('Economic Sustainability')
    envQuality = BooleanField('Local Environmental Quality')
    healthSafety = BooleanField('Enhancing Public Health and Safety')
    resilience = BooleanField('Building Community Resilience')

    allSec = BooleanField('All Sectors')
    transportation = BooleanField('Vechicles and Transportation')
    energy = BooleanField('Energy')
    waste = BooleanField('Waste and Land Management')

    # cementMan = BooleanField('Cement And Manufacturing')
    # electricity = BooleanField('Electricity')
    # naturalGas = BooleanField('Natural Gas')

    submit = SubmitField()
