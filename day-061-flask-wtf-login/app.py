"""Day 61 - Flask-WTF login form: WTForms 3 fields and validators, CSRF protection,
and rendering forms with Bootstrap-Flask (render_form) instead of the dead Flask-Bootstrap.

Demo credentials (local only): admin@example.com / 12345678

Run with:  flask --app app run
"""
import os
import secrets

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", secrets.token_hex(16))
app.config["BOOTSTRAP_SERVE_LOCAL"] = True
Bootstrap5(app)

DEMO_EMAIL, DEMO_PASSWORD = "admin@example.com", "12345678"


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Log In")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        ok = form.email.data == DEMO_EMAIL and form.password.data == DEMO_PASSWORD
        return render_template("success.html" if ok else "denied.html")
    return render_template("login.html", form=form)
