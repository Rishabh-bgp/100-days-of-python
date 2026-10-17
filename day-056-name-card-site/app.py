"""Day 56 - Name Card website: render_template and static files (CSS) with Flask.

Run with:  flask --app app run
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", name="Rishabh Aryan", role="Engineer · Python developer")


if __name__ == "__main__":
    app.run(debug=True)
