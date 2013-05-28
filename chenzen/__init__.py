from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

chenzen = Flask(__name__)
chenzen.config.from_object('config')
db = SQLAlchemy(chenzen)
base_url = 'http://chenzen.org'
login_manager = LoginManager()
login_manager.setup_app(chenzen)
chenzen.secret_key = 'wtf'

from chenzen import views, models


