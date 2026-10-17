"""Day 55 - Higher or Lower (URLs): guess a number by visiting /<number>; URL variables,
converters, returning HTML, and decorators that wrap the HTML.

Run with:  flask --app app run   then open http://127.0.0.1:5000/
"""
import os
import random
from functools import wraps

from flask import Flask

app = Flask(__name__)
SECRET = int(os.environ.get("SECRET_NUMBER", random.randint(0, 9)))


def make_bold(fn):
    @wraps(fn)
    def wrapper(*a, **kw):
        return f"<b>{fn(*a, **kw)}</b>"
    return wrapper


def make_emphasis(fn):
    @wraps(fn)
    def wrapper(*a, **kw):
        return f"<em>{fn(*a, **kw)}</em>"
    return wrapper


@app.route("/")
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<p>Add your guess to the URL, e.g. <code>/5</code></p>"
            "<p style='font-size:80px'>🔢</p>")


@app.route("/<int:guess>")
def check(guess: int):
    if guess > SECRET:
        return "<h1 style='color: purple'>Too high, try again!</h1><p style='font-size:80px'>⬆️</p>"
    if guess < SECRET:
        return "<h1 style='color: red'>Too low, try again!</h1><p style='font-size:80px'>⬇️</p>"
    return "<h1 style='color: green'>You found me!</h1><p style='font-size:80px'>🎉</p>"


@app.route("/greet/<name>/<int:age>")
@make_bold
@make_emphasis
def greet(name: str, age: int):
    return f"Hello {name}, you are {age} years old!"


if __name__ == "__main__":
    app.run(debug=True)
