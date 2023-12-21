# -*- encoding: utf-8 -*-
from typing import *
from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html', route='index')


@app.route('/gif')
def gif():
    return render_template('gif.html', route='gif')


@app.route('/login')
def login():
    return render_template('user/login.html', route='login')


@app.route('/signup')
def signup():
    return render_template('user/signup.html', route='signup')
