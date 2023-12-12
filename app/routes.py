# -*- encoding: utf-8 -*-
from typing import *
from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')
