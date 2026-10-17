"""Day 69 - Blog Capstone part 4: users and comments. Register/login (Flask-Login,
hashed passwords), an @admin_only decorator (the first registered user is the admin who
can create, edit and delete posts), relational tables (User 1-many BlogPost/Comment) and
comments on posts.

Users live in this app's own local SQLite db. Gravatar is replaced with local
initials avatars, so no external service is used.

Run with:  flask --app app run
"""
import os
import secrets
from datetime import date
from functools import wraps

from flask import Flask, abort, flash, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms import EmailField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import URL, DataRequired, Email, Length, Optional


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", secrets.token_hex(16))
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///blog.db")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True
Bootstrap5(app)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(200))
    name: Mapped[str] = mapped_column(String(100))
    posts: Mapped[list["BlogPost"]] = relationship(back_populates="author")
    comments: Mapped[list["Comment"]] = relationship(back_populates="comment_author")

    @property
    def initials(self) -> str:
        return "".join(p[0] for p in self.name.split()[:2]).upper() or "?"


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped[User] = relationship(back_populates="posts")
    title: Mapped[str] = mapped_column(String(250), unique=True)
    subtitle: Mapped[str] = mapped_column(String(250))
    date: Mapped[str] = mapped_column(String(250))
    body: Mapped[str] = mapped_column(Text)
    img_url: Mapped[str] = mapped_column(String(250), default="")
    comments: Mapped[list["Comment"]] = relationship(back_populates="parent_post", cascade="all, delete-orphan")


class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    comment_author: Mapped[User] = relationship(back_populates="comments")
    post_id: Mapped[int] = mapped_column(ForeignKey("blog_posts.id"))
    parent_post: Mapped[BlogPost] = relationship(back_populates="comments")


class RegisterForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


class PostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL (optional)", validators=[Optional(), URL()])
    body = TextAreaField("Blog Content", validators=[DataRequired()], render_kw={"rows": 8})
    submit = SubmitField("Submit Post")


class CommentForm(FlaskForm):
    comment_text = TextAreaField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id: str):
    return db.session.get(User, int(user_id))


def admin_only(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return fn(*args, **kwargs)
    return wrapper


@app.route("/")
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.id.desc())).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data.lower()
        if db.session.execute(db.select(User).where(User.email == email)).scalar():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))
        user = User(email=email, name=form.name.data,
                    password=generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=8))
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for("get_all_posts"))
    return render_template("form.html", form=form, heading="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data.lower())).scalar()
        if not user or not check_password_hash(user.password, form.password.data):
            flash("Wrong email or password, please try again.")
        else:
            login_user(user)
            return redirect(url_for("get_all_posts"))
    return render_template("form.html", form=form, heading="Log In")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("get_all_posts"))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id: int):
    post = db.get_or_404(BlogPost, post_id)
    form = CommentForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to log in or register to comment.")
            return redirect(url_for("login"))
        db.session.add(Comment(text=form.comment_text.data, comment_author=current_user, parent_post=post))
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
    return render_template("post.html", post=post, form=form)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = PostForm()
    if form.validate_on_submit():
        db.session.add(BlogPost(title=form.title.data, subtitle=form.subtitle.data, body=form.body.data,
                                img_url=form.img_url.data or "", author=current_user,
                                date=date.today().strftime("%B %d, %Y")))
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("form.html", form=form, heading="New Post")


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id: int):
    post = db.get_or_404(BlogPost, post_id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("form.html", form=form, heading="Edit Post")


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id: int):
    db.session.delete(db.get_or_404(BlogPost, post_id))
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/protected")
@login_required
def protected():
    return f"Hello {current_user.name}"
