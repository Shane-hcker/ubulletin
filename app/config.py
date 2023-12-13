# -*- encoding: utf-8 -*-
from typing import *
from flask import Config
from sqlalchemy import URL


class AppConfig(Config):
    SQLALCHEMY_DATABASE_URI = URL.create(...)
