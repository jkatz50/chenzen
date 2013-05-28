from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

chenzen = Flask(__name__)
chenzen.config.from_object('config')
db = SQLAlchemy(chenzen)
base_url = 'http://chenzen.org'
chenzen.secret_key = 'wtf'

from chenzen import views, models

login_manager = LoginManager()
login_manager.setup_app(chenzen)


@login_manager.user_loader
def load_user(user_id):
    try:
        user = User.query.get(user_id)
        return User(user)
    except User.DoesNotExist:
        return None