from flask import Flask
# from application import routes
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


from secret_key import app
from sql_key import app

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)