# -*- encoding: utf-8 -*-
from typing import *

from sqlalchemy import Integer, VARCHAR
from flask_login import UserMixin

from app import db, login_manager


@login_manager.user_loader
def get_user(user_id):
    return User.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    # Columns
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    email = db.Column(VARCHAR(48), unique=True, nullable=False)
    username = db.Column(VARCHAR(64), nullable=False)
    password = db.Column()
