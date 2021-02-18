from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tinyfee4_Team:k-k)6ih8URbs@162.241.219.131/tinyfee4_sources'
# :3306
SQLALCHEMY_POOL_RECYCLE=900 #attempts to solve timeout error
db = SQLAlchemy(app)

# --------------------------------- ORM -------------------------------- #

class cement_and_manufacturing(db.Model):
    zip = db.Column(db.Integer, primary_key=True)
    assumedPopulation = db.Column(db.Integer)
    CO2e_MetricTonsPerYear = db.Column(db.Float)

class electricity(db.Model):
    zip = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer)
    service = db.Column(db.Text)
    state = db.Column(db.Text)
    primary_city = db.Column(db.Text)
    zip_type = db.Column(db.Text)
    service_pop = db.Column(db.Integer)
    zip_pop = db.Column(db.Integer)
    zip_business_pop_industrial_service = db.Column(db.Integer)
    zip_business_pop_industrial = db.Column(db.Integer)
    commercial_business_zip_pop = db.Column(db.Integer)
    service_commercial_zip_pop = db.Column(db.Integer)
    cntrl_area = db.Column(db.Text)
    residential_sales_mwh = db.Column(db.Text)
    industrial_sales_mwh = db.Column(db.Text)
    commercial_sales_mwh = db.Column(db.Text)
    commercial_co2e_service_total = db.Column(db.Float)
    commercial_co2e_kg_per_year_per_zip = db.Column(db.Float)
    commercial_co2e_metric_tons_per_year_per_zip = db.Column(db.Float)
    industrial_co2e_service_total = db.Column(db.Float)
    industrial_co2e_kg_per_year_per_zip = db.Column(db.Float)
    industrial_co2e_metric_tons_per_year_per_zip = db.Column(db.Float)
    residential_co2e_service_total = db.Column(db.Float)
    residential_co2e_kg_per_year_per_zip = db.Column(db.Float)
    residential_co2e_metric_tons_per_year_per_zip = db.Column(db.Float)

class natural_gas(db.Model):
    zip = db.Column(db.Integer, primary_key=True)
    residential_volume = db.Column(db.Float)
    commercial_volume = db.Column(db.Float)
    industrial_volume = db.Column(db.Float)

class otis_transportation(db.Model):
    zip = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.Integer)
    city = db.Column(db.Text)
    population = db.Column(db.Integer)
    CO2e_total_passenger_vehicles_gasoline_mT_per_year = db.Column(db.Float)
    CO2e_total_passenger_vehicles_diesel_mT_per_year = db.Column(db.Float)
    CO2e_total_trucks_gasoline_mT_per_year = db.Column(db.Float)
    CO2e_total_trucks_diesel_mT_per_year = db.Column(db.Float)

class waste(db.Model):
    zip = db.Column(db.Integer, primary_key=True)
    assumed_population = db.Column(db.Integer)
    CO2e_MetricTonsPerYear = db.Column(db.Float)

class zip_pop(db.Model):
    zip_id = db.Column(db.Integer, primary_key=True)
    zip = db.Column(db.Integer)
    state = db.Column(db.Text)
    city = db.Column(db.Text)
    type = db.Column(db.Text)
    population2018 = db.Column(db.Integer)
    county = db.Column(db.Text)


# -------------------------------- Page Routes ------------------------------- #

# INDEX
@app.route('/')
def index():
    return render_template('index.html')


# READ
@app.route('/read')
def read():
    Cement_And_Manufacturing = cement_and_manufacturing.query.all()
    Electricity = electricity.query.all()
    Natural_gas = natural_gas.query.all()
    OTIS_Transportation = otis_transportation.query.all()
    Waste = waste.query.all()
    Zip_pop = zip_pop.query.all()
    return render_template('read.html', 
        Cement_And_Manufacturing=Cement_And_Manufacturing, 
        Electricity=Electricity,
        Natural_gas=Natural_gas,
        OTIS_Transportation=OTIS_Transportation,
        Waste=Waste,
        Zip_pop=Zip_pop
        )


@app.errorhandler(404)
def err404(err):
    return render_template('404.html', err=err)


if __name__ == '__main__':
    app.run(debug=True)


















    