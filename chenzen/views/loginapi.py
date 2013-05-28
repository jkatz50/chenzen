from chenzen import chenzen, db
from chenzen.models import User
from chenzen.forms import LoginForm
from flask.views import MethodView
from flask import request
from flask import redirect
from flask import render_template
from flask.ext.login import login_required
from flask.ext.login import logout_user
from flask.ext.login import current_user
from flask.ext.wtf import Form
from flask.ext.wtf import TextField
from flask.ext.wtf import PasswordField
from flask.ext.wtf import Required



import json


class LoginAPI(MethodView):

#login_manager = LoginManager()
    def get(self, id):
    	form = LoginForm()
    	return render_template('login.html', 
        title = 'Sign In',
        form = form)

    #   form = LoginForm()
    #   if form.validate_on_submit():
     #  		try:
       		#	user = User.objects.get(username=request.form['username'])
    	
       			#connect to db and query username and password....

       		#	login_user(user)
       		#	flash('Logged In', 'success')