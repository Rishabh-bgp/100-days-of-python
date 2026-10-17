"""Day 58 - TinDog: a Bootstrap 5 landing page (navbar, hero, features, pricing cards,
testimonial carousel, footer).

Offline: served by Flask with Bootstrap-Flask's bundled Bootstrap files
(BOOTSTRAP_SERVE_LOCAL), so no CDN or internet is needed.

Run with:  flask --app app run
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config["BOOTSTRAP_SERVE_LOCAL"] = True
Bootstrap5(app)

PLANS = [
    {"name": "Chihuahua", "price": "Free", "features": ["5 matches per day", "10 messages per day", "Unlimited app usage"]},
    {"name": "Labrador", "price": "₹499 / mo", "features": ["Unlimited matches", "Unlimited messages", "Unlimited app usage"]},
    {"name": "Mastiff", "price": "₹999 / mo", "features": ["Priority listing", "Unlimited matches", "Unlimited messages"]},
]


@app.route("/")
def home():
    return render_template("index.html", plans=PLANS)
