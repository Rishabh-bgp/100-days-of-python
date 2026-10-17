"""Day 95 - Portfolio project: an API-based website. The page is a small single-page app
that fetches JSON from an API and renders it (random quote, search by tag, list all).

API-free in the sense of 'no external service': the API is served by this same Flask app
from bundled quotes.json, so the whole thing runs offline with no key.

Run with:  flask --app app run    API:  /api/quotes, /api/quotes/random, /api/quotes?tag=python
"""
import json
import random
from pathlib import Path

from flask import Flask, abort, jsonify, render_template, request

app = Flask(__name__)
QUOTES = json.loads(Path(__file__).with_name("quotes.json").read_text(encoding="utf-8"))


@app.route("/")
def home():
    tags = sorted({t for q in QUOTES for t in q["tags"]})
    return render_template("index.html", tags=tags)


@app.get("/api/quotes")
def list_quotes():
    tag = request.args.get("tag")
    return jsonify(quotes=[q for q in QUOTES if not tag or tag in q["tags"]])


@app.get("/api/quotes/random")
def random_quote():
    return jsonify(quote=random.choice(QUOTES))


@app.get("/api/quotes/<int:quote_id>")
def get_quote(quote_id: int):
    quote = next((q for q in QUOTES if q["id"] == quote_id), None)
    return jsonify(quote=quote) if quote else abort(404)
