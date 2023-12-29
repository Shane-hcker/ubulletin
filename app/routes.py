# -*- encoding: utf-8 -*-
from typing import *
from flask import render_template

from app import app
from app.forms import *


@app.route('/')
def index():
    return render_template('index.html', route='index')


@app.route('/gif')
def gif():
    return render_template('gif.html', route='gif')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('user/login.html', route='login', login=LoginForm(), 
                           signup=SignupForm())
