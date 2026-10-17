"""Day 59 - Blog Capstone part 2: a styled multi-page blog (home, post, about, contact)
using template inheritance and Bootstrap 5 (served locally via Bootstrap-Flask).

Run with:  flask --app app run
"""
import json
from pathlib import Path

from flask import Flask, abort, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config["BOOTSTRAP_SERVE_LOCAL"] = True
Bootstrap5(app)
POSTS = json.loads(Path(__file__).with_name("posts.json").read_text(encoding="utf-8"))


@app.route("/")
def home():
    return render_template("index.html", posts=POSTS)


@app.route("/post/<int:post_id>")
def post(post_id: int):
    found = next((p for p in POSTS if p["id"] == post_id), None)
    return render_template("post.html", post=found) if found else abort(404)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
