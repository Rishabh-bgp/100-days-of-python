"""Day 54 - Intro to Flask: your first web server, routes, and how decorators work.

Run with:  flask --app app run --debug
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1><p>This page is served by Flask.</p>"


@app.route("/bye")
def say_bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
