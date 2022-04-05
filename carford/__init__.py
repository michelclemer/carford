# Import flask and template operators
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)

from carford.controllers.carford_controller import model_carford

app.register_blueprint(model_carford)

db.create_all()
