from chenzen import chenzen
from chenzen.models import Users
from flask.views import MethodView
from flask import request
import json


class LoginAPI(MethodView):

    def get(self, id):
        if id is None:
        	users = Users.query.all()
            pass
        else:
            pass
