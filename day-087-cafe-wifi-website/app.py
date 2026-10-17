"""Day 87 - Portfolio project: Cafe & Wi-Fi website. Browse, filter, add and delete
work-friendly cafes stored in SQLite (Flask 3 + Flask-SQLAlchemy 3.1 + WTForms 3 +
Bootstrap-Flask). Seeded with fictional cafes on first run.

Run with:  flask --app app run
"""
import os
import secrets

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import URL, DataRequired


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", secrets.token_hex(16))
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///cafes.db")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True
Bootstrap5(app)
db.init_app(app)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True)
    map_url: Mapped[str] = mapped_column(String(500))
    location: Mapped[str] = mapped_column(String(250))
    seats: Mapped[str] = mapped_column(String(50))
    has_wifi: Mapped[bool] = mapped_column(Boolean)
    has_sockets: Mapped[bool] = mapped_column(Boolean)
    can_take_calls: Mapped[bool] = mapped_column(Boolean)
    coffee_price: Mapped[str] = mapped_column(String(50))


class CafeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    map_url = StringField("Map URL", validators=[DataRequired(), URL()])
    location = StringField("Area", validators=[DataRequired()])
    seats = StringField("Seats (e.g. 20-30)", validators=[DataRequired()])
    coffee_price = StringField("Coffee price (e.g. ₹150)", validators=[DataRequired()])
    has_wifi = BooleanField("Wi-Fi")
    has_sockets = BooleanField("Power sockets")
    can_take_calls = BooleanField("OK to take calls")
    submit = SubmitField("Add cafe")


SEED = [("Sample Roasters", "Arera Colony", "20-30", True, True, False, "₹180"),
        ("Byte Brew", "MG Road", "30-40", True, True, True, "₹150"),
        ("Lakeside Beans", "Lake View", "10-20", True, False, True, "₹220"),
        ("The Quiet Cup", "New Market", "10-20", False, True, False, "₹120")]

with app.app_context():
    db.create_all()
    if not db.session.execute(db.select(Cafe)).first():
        for name, loc, seats, wifi, sockets, calls, price in SEED:
            db.session.add(Cafe(name=name, map_url=f"https://maps.example.com/{name.lower().replace(' ', '-')}",
                                location=loc, seats=seats, has_wifi=wifi, has_sockets=sockets,
                                can_take_calls=calls, coffee_price=price))
        db.session.commit()


@app.route("/")
def home():
    query = db.select(Cafe).order_by(Cafe.name)
    for flag in ("has_wifi", "has_sockets", "can_take_calls"):
        if request.args.get(flag):
            query = query.where(getattr(Cafe, flag).is_(True))
    if area := request.args.get("area"):
        query = query.where(Cafe.location.ilike(f"%{area}%"))
    return render_template("index.html", cafes=db.session.execute(query).scalars().all(), args=request.args)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = Cafe()
        form.populate_obj(cafe)
        db.session.add(cafe)
        db.session.commit()
        flash(f"Added {cafe.name}")
        return redirect(url_for("home"))
    return render_template("add.html", form=form)


@app.route("/delete/<int:cafe_id>", methods=["POST"])
def delete(cafe_id: int):
    db.session.delete(db.get_or_404(Cafe, cafe_id))
    db.session.commit()
    return redirect(url_for("home"))
