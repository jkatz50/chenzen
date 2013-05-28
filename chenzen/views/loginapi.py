from chenzen import chenzen, db
from chenzen.models import User
from flask.views import MethodView
from flask import request
from flask import redirect
from flask import render_template
from flask.ext.login import login_required
from flask.ext.login import logout_user
from flask.ext.login import current_user


import json


class LoginAPI(MethodView):

#login_manager = LoginManager()
    def get(self, id):
    #   form = LoginForm()
    #   if form.validate_on_submit():
     #  		try:
       		#	user = User.objects.get(username=request.form['username'])
    	print "test"
       			#connect to db and query username and password....

       		#	login_user(user)
       		#	flash('Logged In', 'success')