from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.sql import func

from carford import db


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    data_created = db.Column(DateTime(timezone=True), default=func.now())
    date_modified = db.Column(DateTime(timezone=True), default=func.now())


class User(Base):

    __tablename__ = "user"

    name = db.Column(db.String(128), nullable=False)

    email = db.Column(db.String(128), nullable=False, unique=True)

    carro_id = db.Column(db.Integer, ForeignKey('car.id'))




    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.name


class Car(Base):
    __tablename__ = "car"


    name = db.Column(db.String(128), nullable=False)

    cor = db.Column(db.String(128), nullable=False, unique=True)

    marca = db.Column(db.String(128), nullable=False)

