from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

chenzen = Flask(__name__)
chenzen.config.from_object('config')
db = SQLAlchemy(chenzen)
base_url = 'http://chenzen.org'

from chenzen import views, models
