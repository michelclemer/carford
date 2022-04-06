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
from flask_sqlalchemy import inspect
from flask.views import MethodView
from carford import db
from carford.models.form import FormLogin
from carford.models.carford_model import User

model_carford = Blueprint("carford", __name__)


@model_carford.route("/")
@model_carford.route("/home")
def view_page():
    return "Cadastro"


class CadastroPropietario(MethodView):
    def get(self):
        form = FormLogin(request.form)
        return render_template("home_page.html", form=form)

    def post(self):

        nome = request.form.get("nome")
        email = request.form.get("email")
        carro = request.form.get("carro")
        tipo_carro = request.form.get("tipo_carro")
        cor_carro = request.form.get("cor_carro")
        user_exist = User.query.filter_by(email=email).count()

        if user_exist is None:
            print("Não existe")
        if user_exist < 3:
            tipo_carro_db = User.query.filter_by(
                tipo_carro=tipo_carro, email=email
            ).count()
            if tipo_carro_db == 0:
                user = User(nome, email, carro, tipo_carro, cor_carro)
                db.session.add(user)
                db.session.commit()
                print(nome, email, carro, tipo_carro, cor_carro)
            else:
                print("Tipo de carro não disponível")
        else:
            return render_template("user_error.html")

        return render_template("cadastro_ok.html")


@model_carford.route("/lista", methods=["GET"])
def listar():
    return render_template("lista.html")
