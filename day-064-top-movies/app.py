"""Day 64 - My Top 10 Movies: Flask + SQLAlchemy CRUD with WTForms, ranking movies by
rating, and a two-step 'search then select' add flow.

API-free: the course searches TMDB (API key) for movie details and posters. Here the
search runs over a bundled catalogue.json (titles, years, short original descriptions),
and posters are drawn as coloured placeholders.

Run with:  flask --app app run
"""
import json
import os
import secrets
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange

CATALOGUE = json.loads(Path(__file__).with_name("catalogue.json").read_text(encoding="utf-8"))


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", secrets.token_hex(16))
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///movies.db")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True
Bootstrap5(app)
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(500))
    rating: Mapped[float | None] = mapped_column(Float, nullable=True)
    ranking: Mapped[int | None] = mapped_column(Integer, nullable=True)
    review: Mapped[str | None] = mapped_column(String(250), nullable=True)


class RateMovieForm(FlaskForm):
    rating = FloatField("Your rating out of 10, e.g. 7.5", validators=[DataRequired(), NumberRange(0, 10)])
    review = StringField("Your review")
    submit = SubmitField("Done")


class FindMovieForm(FlaskForm):
    title = StringField("Movie title", validators=[DataRequired()])
    submit = SubmitField("Search")


def search_catalogue(query: str) -> list[dict]:
    q = query.lower().strip()
    return [m for m in CATALOGUE if q in m["title"].lower()]


with app.app_context():
    db.create_all()
    if not db.session.execute(db.select(Movie)).first():
        db.session.add(Movie(title="Phone Booth", year=2002, description=CATALOGUE[0]["description"],
                             rating=7.3, review="My favourite character was the caller."))
        db.session.commit()


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    for i, movie in enumerate(movies):
        movie.ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        return render_template("select.html", options=search_catalogue(form.title.data))
    return render_template("add.html", form=form)


@app.route("/find")
def find():
    chosen = next((m for m in CATALOGUE if m["title"] == request.args.get("title")), None)
    if chosen is None:
        return redirect(url_for("add"))
    existing = db.session.execute(db.select(Movie).where(Movie.title == chosen["title"])).scalar()
    movie = existing or Movie(**chosen)
    if not existing:
        db.session.add(movie)
        db.session.commit()
    return redirect(url_for("edit", id=movie.id))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie = db.get_or_404(Movie, request.args.get("id", type=int))
    form = RateMovieForm()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie = db.get_or_404(Movie, request.args.get("id", type=int))
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))
