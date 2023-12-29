# -*- encoding: utf-8 -*-
from typing import *
from functools import wraps

import sqlalchemy
from sqlalchemy import and_
from flask_wtf import FlaskForm
from wtforms import Field, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app import db
from app.models import User


__all__ = ['LoginForm', 'SignupForm']

ILLEGAL_CHAR = {'--', '\'', '\"'}


def valid_char(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        val = args[-1].data
        for char in ILLEGAL_CHAR:
            if char in val:
                raise ValidationError('Illegal characters: \", \', --')
        return func(*args, **kwargs)
    return wrapper


class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email(check_deliverability=True)])
    password = PasswordField(validators=[DataRequired(), Length(min=8)])
    # remember = BooleanField('Remember Me')
    submit = SubmitField()

    @valid_char
    def validate_email(self, email: Field):
        if not email.data.endswith('@uwcchina.org'):
            raise ValidationError(f'{email.data} is not a school email.')


class SignupForm(LoginForm):
    username = StringField(validators=[DataRequired(), Length(min=4, max=16)])
    confirm_password = PasswordField(validators=[DataRequired(), Length(min=8)])
    # remember = None

    @valid_char
    def validate_username(self, username):
        pass
    
    @valid_char
    def validate_email(self, email: Field):
        super().validate_email(email)
        if db.session.scalars(sqlalchemy.select(User).where(User.email == email.data)):
            raise ValidationError('This email has been registered.')

    @valid_char
    def validate_confirm_password(self, confirm_password):
        if self.password.data != confirm_password.data:
            raise ValidationError('Unidentical Password Pair')
