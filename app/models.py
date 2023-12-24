# -*- encoding: utf-8 -*-
from typing import *

from sqlalchemy import Integer, VARCHAR, Text as sText
from flask_login import UserMixin
from flask_wtf import FlaskForm

from app import db, login_manager
from app.datatypes import *
from app.mixins import *


__all__ = ['User', 'Post']


@login_manager.user_loader
def get_user(user_id):
    return User.get(int(user_id))


class User(UserMixin, DBMixin, db.Model):
    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(VARCHAR(48), unique=True, nullable=False)
    username = Column(VARCHAR(64), nullable=False)
    password = Column(SaltVarChar(102), nullable=False)

    post = db.relationship('Post', backref='user', lazy=True)

    def to_dict(self) -> MutableMapping:
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'password': self.password
        }

    @classmethod
    def new(cls, **kwargs) -> "User":
        _new_user = cls()
        _new_user.email = kwargs.get('email')
        _new_user.username = kwargs.get('username')
        _new_user.password = kwargs.get('password')
        return _new_user

    @classmethod
    def from_form(cls, form: FlaskForm) -> "User":
        _new_user = cls()
        _new_user.email = form.email.data
        _new_user.username = form.username.data
        _new_user.password = form.password.data
        return _new_user

    def __str__(self) -> str:
        return f"<User \"{self.username}\">"

    __repr__ = __str__


class Post(DBMixin, db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(sText)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __str__(self) -> str:
        return f'<Post By: {self.get(self.user_id)}>'
