"""Day 62 - Coffee & Wi-Fi: a Flask-WTF form with URL validation and select fields that
appends cafes to a CSV, plus a table page that renders the CSV.

Run with:  flask --app app run
"""
import csv
import os
import secrets
from pathlib import Path

from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import URL, DataRequired

CSV_PATH = Path(__file__).with_name("cafe-data.csv")
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", secrets.token_hex(16))
app.config["BOOTSTRAP_SERVE_LOCAL"] = True
Bootstrap5(app)


def rating(symbol: str, allow_zero: bool = False) -> list[str]:
    return (["✘"] if allow_zero else []) + [symbol * i for i in range(1, 6)]


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField("Cafe location on a map (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening time, e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing time, e.g. 5:30PM", validators=[DataRequired()])
    coffee = SelectField("Coffee rating", choices=rating("☕"))
    wifi = SelectField("Wifi strength", choices=rating("💪", allow_zero=True))
    power = SelectField("Power socket availability", choices=rating("🔌", allow_zero=True))
    submit = SubmitField("Submit")


def read_cafes() -> list[list[str]]:
    with open(CSV_PATH, newline="", encoding="utf-8") as fh:
        return list(csv.reader(fh))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open(CSV_PATH, "a", newline="", encoding="utf-8") as fh:
            csv.writer(fh).writerow([form.cafe.data, form.location.data, form.open.data, form.close.data,
                                     form.coffee.data, form.wifi.data, form.power.data])
        return redirect(url_for("cafes"))
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    return render_template("cafes.html", cafes=read_cafes())
