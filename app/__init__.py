# -*- encoding: utf-8 -*-
from typing import *
import flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = flask.Flask(__name__)

from app.config import AppConfig

app.config.from_object(AppConfig)
login_manager = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models, forms
