from chenzen import chenzen, db, login_manager
from chenzen.models import User
from chenzen.forms import LoginForm
from flask.views import MethodView
from flask import request
from flask import redirect, session, url_for, g
from flask import render_template
from flask.ext.login import login_user
from flask.ext.login import login_required
from flask.ext.login import logout_user
from flask.ext.login import current_user

import json


class LoginAPI(MethodView):

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))

  def get(self, id):
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
      session['remember_me'] = form.remember_me.data
      

    return render_template('login.html', 
        title = 'Sign In',
        form = form)

  def post(self):
    username = request.form['username']
    password =  (request.form['password'])
    user = User.query.filter_by(username=username).first()
    if user:
      print "COOL"
      if login_user(User(user)):
        flash("You have loggedin")

