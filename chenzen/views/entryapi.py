from chenzen import chenzen, db
from chenzen.models import Entry
from flask.views import MethodView
from flask import request
import json


class EntryAPI(MethodView):

    def get(self, id):
        if id is None:
            pass
        else:
            pass

    def post(self):
        pass

    def delete(self, id):
        pass
