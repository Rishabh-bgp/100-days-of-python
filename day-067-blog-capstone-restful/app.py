"""Day 67 - Blog Capstone part 3: a RESTful blog with full CRUD (create, read, update,
delete) on SQLite via Flask-SQLAlchemy 3.1, using WTForms 3 + Bootstrap-Flask.

The course uses Flask-CKEditor for rich text; this uses a plain textarea whose text is
rendered with line breaks (no extra dependency).

Run with:  flask --app app run
"""
import os
import secrets
from datetime import date

from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import URL, DataRequired, Optional


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", secrets.token_hex(16))
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///posts.db")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True
Bootstrap5(app)
db.init_app(app)


class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False, default="")


class PostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL (optional)", validators=[Optional(), URL()])
    body = TextAreaField("Blog Content", validators=[DataRequired()], render_kw={"rows": 10})
    submit = SubmitField("Submit Post")


with app.app_context():
    db.create_all()
    if not db.session.execute(db.select(BlogPost)).first():
        db.session.add(BlogPost(title="Hello, RESTful world", subtitle="The first post", date=date.today().strftime("%B %d, %Y"),
                                body="This post lives in SQLite.\nEdit or delete it from the post page.", author="Rishabh"))
        db.session.commit()


@app.route("/")
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.id.desc())).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id: int):
    return render_template("post.html", post=db.get_or_404(BlogPost, post_id))


@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = BlogPost(title=form.title.data, subtitle=form.subtitle.data, body=form.body.data,
                        img_url=form.img_url.data or "", author=form.author.data,
                        date=date.today().strftime("%B %d, %Y"))
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, is_edit=False)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id: int):
    post = db.get_or_404(BlogPost, post_id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=form, is_edit=True)


@app.route("/delete/<int:post_id>")
def delete_post(post_id: int):
    db.session.delete(db.get_or_404(BlogPost, post_id))
    db.session.commit()
    return redirect(url_for("get_all_posts"))
