# -*- encoding: utf-8 -*-
from typing import *
from app import app
from flask import render_template


@app.route('/gif')
def gif():
    return render_template('gif.html', route='gif')
