# -*- encoding: utf-8 -*-
from typing import *
import os
import random
from flask import Config
from sqlalchemy import URL


def secret_key() -> str:
    return ''.join([chr(random.randint(48, 122)) for _ in range(32)])


class AppConfig(Config):
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or secret_key()

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = URL.create('mysql+pymysql', host='localhost', port=3306,
                                         username='root', database='ubulletin', password='12345678')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
