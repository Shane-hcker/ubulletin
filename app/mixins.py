# -*- encoding: utf-8 -*-
from typing import *
from app import db

import sqlalchemy


__all__ = ['DBMixin']


class DBMixin:
    def commit(self):
        db.session.commit()
        return self

    @classmethod
    def all(cls):
        return db.session.scalars(sqlalchemy.select(cls)).all()

    @classmethod
    def get(cls, obj_id: int):
        return db.session.get(cls, obj_id)

    def add(self, _warn: bool = True) -> Self:
        db.session.add(self, _warn)
        return self
