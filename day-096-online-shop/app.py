"""Day 96 - Portfolio project: online shop. Product catalogue, a session-based cart
(add / update quantity / remove), stock checks, and a checkout that creates an order.

Account-free: the course takes payments with Stripe (account + keys). Here checkout is a
MOCK payment step: you enter any name/email and a fake card number; it validates the
format with the Luhn check (try 4242 4242 4242 4242), then records the order in local
SQLite. No money moves and nothing leaves your machine.

Run with:  flask --app app run
"""
import json
import os
import secrets
from datetime import datetime
from pathlib import Path

from flask import Flask, abort, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

PRODUCTS = {p["id"]: p for p in json.loads(Path(__file__).with_name("products.json").read_text(encoding="utf-8"))}


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", secrets.token_hex(16))
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///shop.db")
db.init_app(app)


class Order(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created: Mapped[str] = mapped_column(String(30))
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(120))
    items_json: Mapped[str] = mapped_column(Text)
    total: Mapped[int] = mapped_column(Integer)
    card_last4: Mapped[str] = mapped_column(String(4))


with app.app_context():
    db.create_all()


def luhn_ok(number: str) -> bool:
    digits = [int(d) for d in number if d.isdigit()]
    if len(digits) < 12:
        return False
    checksum = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2:
            d = d * 2 - 9 if d * 2 > 9 else d * 2
        checksum += d
    return checksum % 10 == 0


def cart() -> dict[str, int]:
    return session.setdefault("cart", {})


def cart_lines() -> tuple[list[dict], int]:
    lines = [{**PRODUCTS[int(pid)], "qty": qty, "subtotal": PRODUCTS[int(pid)]["price"] * qty}
             for pid, qty in cart().items() if int(pid) in PRODUCTS]
    return lines, sum(line["subtotal"] for line in lines)


@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS.values(), count=sum(cart().values()))


@app.post("/cart/add/<int:pid>")
def add_to_cart(pid: int):
    if pid not in PRODUCTS:
        abort(404)
    c = cart()
    qty = c.get(str(pid), 0) + 1
    if qty > PRODUCTS[pid]["stock"]:
        flash("Sorry, not enough stock.")
    else:
        c[str(pid)] = qty
        session.modified = True
        flash(f"Added {PRODUCTS[pid]['name']} to your cart.")
    return redirect(request.referrer or url_for("home"))


@app.post("/cart/update/<int:pid>")
def update_cart(pid: int):
    qty = max(0, min(int(request.form.get("qty", 0)), PRODUCTS.get(pid, {}).get("stock", 0)))
    c = cart()
    if qty:
        c[str(pid)] = qty
    else:
        c.pop(str(pid), None)
    session.modified = True
    return redirect(url_for("view_cart"))


@app.route("/cart")
def view_cart():
    lines, total = cart_lines()
    return render_template("cart.html", lines=lines, total=total)


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    lines, total = cart_lines()
    if not lines:
        return redirect(url_for("home"))
    if request.method == "POST":
        card = request.form.get("card", "")
        if not luhn_ok(card):
            flash("That card number isn't valid (try the test number 4242 4242 4242 4242).")
            return render_template("checkout.html", total=total)
        order = Order(created=datetime.now().isoformat(timespec="seconds"), name=request.form["name"],
                      email=request.form["email"], total=total, card_last4="".join(filter(str.isdigit, card))[-4:],
                      items_json=json.dumps([{"id": line["id"], "qty": line["qty"]} for line in lines]))
        db.session.add(order)
        for line in lines:
            PRODUCTS[line["id"]]["stock"] -= line["qty"]
        db.session.commit()
        session["cart"] = {}
        return redirect(url_for("success", order_id=order.id))
    return render_template("checkout.html", total=total)


@app.route("/success/<int:order_id>")
def success(order_id: int):
    return render_template("success.html", order=db.get_or_404(Order, order_id))
