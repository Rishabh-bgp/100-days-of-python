"""A local stand-in for Google Forms: three questions, answers appended to responses.csv.

Run alone:  flask --app form_site run   then open http://127.0.0.1:5000
"""
import csv
from pathlib import Path

from flask import Flask, redirect, request

app = Flask(__name__)
RESPONSES = Path(__file__).with_name("responses.csv")

FORM = """<!doctype html><html><head><meta charset="utf-8"><title>Rental research form</title></head><body>
<h1>Rental research (local form)</h1><form method="post">
<label>Property address <input name="address" required></label><br>
<label>Price per month <input name="price" required></label><br>
<label>Link to property <input name="link" required></label><br>
<button type="submit" id="submit">Submit</button></form></body></html>"""


@app.get("/")
def form():
    return FORM


@app.post("/")
def submit():
    new = not RESPONSES.exists()
    with open(RESPONSES, "a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["address", "price", "link"])
        w.writerow([request.form["address"], request.form["price"], request.form["link"]])
    return redirect("/thanks")


@app.get("/thanks")
def thanks():
    return '<p id="thanks">Your response has been recorded.</p><a id="again" href="/">Submit another response</a>'
