from flask import (
    Blueprint,
    request,
    render_template,
    flash,
    g,
    session,
    redirect,
    url_for,
)
from carford import db
from carford.models.form import FormLogin
from carford.models.carford_model import User

model_carford = Blueprint("carford", __name__, url_prefix="/carford")


@model_carford.route("/", methods=["GET", "POST"])
def view_page():

    form = FormLogin(request.form)
    print(request.form.get("cor_carro"))
    print(request.form.items())
    print(request.form)
    return render_template("home_page.html", form=form)


@model_carford.route("/lista", methods=["GET"])
def listar():
    return render_template("lista.html")
