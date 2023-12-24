# -*- encoding: utf-8 -*-
from typing import *

from sqlalchemy import VARCHAR,TypeDecorator
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


__all__ = ['SaltPassword', 'SaltVarChar', 'SaltStr', 'Column', 'ForeignKey']


class SaltPassword(str):
    def is_(self, other: str) -> bool:
        """
        determine whether the string is the hash of param `other`
        :param other: the password to compare with
        """
        return check_password_hash(self, other)

    @classmethod
    def wrap(cls, saltypassword: str) -> Self:
        """
        wraps salt password with ``SaltPassword``
        :param saltypassword: saltypassword to wrap
        """
        return cls(saltypassword)

    @classmethod
    def saltify(cls, original: str) -> Self:
        """
        saltify a password with ``SaltPassword()``
        :param original: the original password
        """
        return cls(generate_password_hash(original))


class SaltVarChar(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, value, dialect) -> Optional[str]:
        return SaltPassword.saltify(value)

    def process_result_value(self, value, dialect) -> SaltPassword:
        return SaltPassword(value)


SaltStr = TypeVar('SaltStr', SaltPassword, str)
Column = db.Column
ForeignKey = db.ForeignKey
