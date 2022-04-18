from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# from application import routes

from sql_key import app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from secret_key import app

db = SQLAlchemy(app)
