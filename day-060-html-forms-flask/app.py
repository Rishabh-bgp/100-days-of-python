"""Day 60 - HTML forms with Flask: handle POST requests with request.form, a simple
login form, and a contact form that 'emails' the message.

Account-free: the contact form writes to a local outbox/ (or local debug SMTP server via
LOCAL_SMTP=1) instead of logging into Gmail.

Run with:  flask --app app run
"""
from flask import Flask, render_template, request

from outbox import send_email

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    return f"<h1>Name: {request.form['username']}, Password: {'*' * len(request.form['password'])}</h1>"


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email("me@example.com", f"New message from {data['name']}",
                   f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data.get('phone', '')}\nMessage: {data['message']}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
