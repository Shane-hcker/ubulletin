# -*- encoding: utf-8 -*-
from typing import *

from werkzeug.security import generate_password_hash
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user

from app import app, db
from app.models import User
from app.forms import *


@app.route('/')
def index():
    return render_template('index.html', route='index')


@app.route('/gif')
def gif():
    return render_template('gif.html', route='gif')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if (_signup := SignupForm()).is_submitted() and _signup.validate_on_submit():
        login_user(User.new_from_form(_signup).add().commit())
        return redirect(url_for('gif'))

    if (_login := LoginForm()).is_submitted() and _login.validate_on_submit():
        login_user(User.get_user(email=_login.email.data))
        return redirect(url_for('index'))

    return render_template('user/login.html', route='login',
                           login=_login, signup=_signup)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))
