# -*- encoding: utf-8 -*-
from typing import *
import flask


app = flask.Flask(__name__)

from . import routes
