from flask_wtf import Form
from wtforms import TextAreaField, PasswordField, StringField
from wtforms.validators import DataRequired, InputRequired, Length


class FormLogin(Form):
    nome = StringField("Nome", validators=[InputRequired(), Length(min=4, max=50)])
    email = StringField("E-mail", validators=[InputRequired(), Length(min=4, max=50)])
    carro = StringField("Carro", validators=[InputRequired(), Length(min=4, max=50)])
