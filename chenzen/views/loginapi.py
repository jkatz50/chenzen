from chenzen import chenzen
from chenzen.models import Users
from chenzen.forms import LoginForm
from flask.views import MethodView
from flask import request
from flask import redirect
from flask import render_template
from flask.ext.login import login_use
from flask.ext.login import login_required
from flask.ext.login import logout_user
from flask.ext.login import current_user

import json


class LoginAPI(MethodView):

login_manager = 
    def get(self, id):
       form = LoginForm()
       if form.validate_on_submit():
       		try:
       			user = User.objects.get(username=request.form['username'])

       			#connect to db and query username and password....

       			login_user(user)
       			flash('Logged In', 'success')

