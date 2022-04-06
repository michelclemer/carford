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

    email = db.Column(db.String(128), nullable=False)

    carro = db.Column(db.String(128), nullable=False)

    cor_carro = db.Column(db.String(128), nullable=False)

    tipo_carro = db.Column(db.String(128), nullable=False)

    def __init__(self, name, email, carro, tipo_carro, cor_carro):
        self.name = name
        self.email = email
        self.carro = carro
        self.tipo_carro = tipo_carro
        self.cor_carro = cor_carro

    def __repr__(self):
        return "<User %r>" % self.name
