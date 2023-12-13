# -*- encoding: utf-8 -*-
from typing import *
import flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)

from app.config import AppConfig

app.config.from_object(AppConfig)
db = SQLAlchemy(app)
# login_manager = LoginManager(app)


from . import routes
