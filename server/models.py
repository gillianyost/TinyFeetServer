from server import db

# --------------------------------- Sector Tables ORM -------------------------------- #
# For some reason, function names need to be lower case?? Otherwise we get an error

class cement_and_manufacturing(db.Model):
    __tablename__ = 'cement_and_manufacturing'
    zip = db.Column(db.Integer, primary_key=True)
    CO2e_MetricTonsPerYear = db.Column(db.Float)

class electricity(db.Model):
    __tablename__ = 'electricity'
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
    __tablename__ = 'natural_gas'
    zip = db.Column(db.Integer, primary_key=True)
    residential_volume = db.Column(db.Float)
    commercial_volume = db.Column(db.Float)
    industrial_volume = db.Column(db.Float)

class otis_transportation(db.Model):
    __tablename__ = 'otis_transportation'
    zip = db.Column(db.Integer, primary_key=True)
    CO2e_total_passenger_vehicles_gasoline_mT_per_year = db.Column(db.Float)
    CO2e_total_passenger_vehicles_diesel_mT_per_year = db.Column(db.Float)
    CO2e_total_trucks_gasoline_mT_per_year = db.Column(db.Float)
    CO2e_total_trucks_diesel_mT_per_year = db.Column(db.Float)

class waste(db.Model):
    __tablename__ = 'waste'
    zip = db.Column(db.Integer, primary_key=True)
    CO2e_MetricTonsPerYear = db.Column(db.Float)

class aviation(db.Model):
    __tablename__ = 'aviation'
    zip = db.Column(db.Integer, primary_key=True)
    CO2e_metricTonsPerYear = db.Column(db.Float)

class zip_pop(db.Model):
    __tablename__ = 'zip_pop'
    zip_id = db.Column(db.Integer, primary_key=True)
    zip = db.Column(db.Integer)
    state = db.Column(db.Text)
    city = db.Column(db.Text)
    type = db.Column(db.Text)
    population2018 = db.Column(db.Integer)
    county = db.Column(db.Text)

class Zip_data(db.Model):
    __tablename__ = 'v_sectorAllTotalGHG_zip'
    zip = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.Text)
    county = db.Column(db.Text)
    cement_and_manufacturing = db.Column(db.Integer)
    waste = db.Column(db.Integer)
    electricity_commercial = db.Column(db.Integer)
    electricity_industrial = db.Column(db.Integer)
    electricity_residential = db.Column(db.Integer)
    naturalGas_commercial = db.Column(db.Integer)
    naturalGas_industrial = db.Column(db.Integer)
    naturalGas_residential = db.Column(db.Integer)
    transportation_PV_gas = db.Column(db.Integer)
    transportation_PV_diesel = db.Column(db.Integer)
    transportation_trucks_gas = db.Column(db.Integer)
    transportation_trucks_diesel = db.Column(db.Integer)
    aviation = db.Column(db.Integer)
