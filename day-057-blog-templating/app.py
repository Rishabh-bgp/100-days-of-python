"""Day 57 - Templating with Jinja: expressions, for loops, if statements, url_for, and
rendering a blog from JSON data.

API-free: the course fetches blog posts from npoint.io and guesses age/gender via the
agify/genderize APIs. Here posts come from bundled posts.json, and /guess/<name> uses a
small deterministic local function (just for practising templates - it's not a real guess).

Run with:  flask --app app run
"""
import json
import zlib
from datetime import date
from pathlib import Path

from flask import Flask, abort, render_template

app = Flask(__name__)
POSTS = json.loads(Path(__file__).with_name("posts.json").read_text(encoding="utf-8"))


def playful_guess(name: str) -> tuple[int, str]:
    """Stable pseudo-random 'guess' from the name's checksum (offline stand-in for the APIs)."""
    n = zlib.crc32(name.lower().encode())
    return 18 + n % 50, ("female", "male", "non-binary")[n % 3]


@app.route("/")
def home():
    return render_template("index.html", posts=POSTS, year=date.today().year)


@app.route("/guess/<name>")
def guess(name: str):
    age, gender = playful_guess(name)
    return render_template("guess.html", name=name.title(), age=age, gender=gender, year=date.today().year)


@app.route("/post/<int:post_id>")
def post(post_id: int):
    found = next((p for p in POSTS if p["id"] == post_id), None)
    if found is None:
        abort(404)
    return render_template("post.html", post=found, year=date.today().year)


if __name__ == "__main__":
    app.run(debug=True)
