import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tinyfee4_Team:k-k)6ih8URbs@162.241.219.131/tinyfee4_sources'
app.config["SQLALCHEMY_POOL_RECYCLE"] = 280
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'secret'
# :3306
db = SQLAlchemy(app)

# -------------------------------- Blueprints -------------------------------- #
# Must be defined after import db
from server.sectors.views import sectors_blueprint
app.register_blueprint(sectors_blueprint,url_prefix="/sectors")

from server.sectors.export import export_blueprint
app.register_blueprint(export_blueprint,url_prefix="/sectors")

# from server.registration.views import registration_blueprint
# app.register_blueprint(registration_blueprint,url_prefix="/registration")
