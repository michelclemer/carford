# Import flask and template operators
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)

from carford.controllers.carford_controller import model_carford, CadastroPropietario


cadastrar_proprietario = CadastroPropietario.as_view("cadastro_view")
app.add_url_rule(
    "/cadastro/", view_func=cadastrar_proprietario, methods=["GET", "POST"]
)
db.create_all()
