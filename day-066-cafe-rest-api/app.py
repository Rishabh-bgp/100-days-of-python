"""Day 66 - Build your own RESTful API: a cafe database with GET (random, all, search),
POST (add), PATCH (update price) and DELETE (report closed, needs an API key header/param).

This is YOUR local API, so its 'API key' is just a local demo value you choose
(env CAFE_API_KEY, default 'TopSecretAPIKey'); no external service is involved.
Seeded with a few fictional cafes on first run.

Run with:  flask --app app run   then try  curl http://127.0.0.1:5000/random
"""
import os
import random

from flask import Flask, jsonify, render_template_string, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

API_KEY = os.environ.get("CAFE_API_KEY", "TopSecretAPIKey")


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///cafes.db")
db.init_app(app)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str | None] = mapped_column(String(250), nullable=True)

    def to_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


SEED = [
    ("Sample Roasters", "Arera Colony", "20-30", True, True, True, False, "₹180"),
    ("Byte Brew", "MG Road", "30-40", True, True, True, True, "₹150"),
    ("Lakeside Beans", "Lake View", "10-20", False, True, False, True, "₹220"),
]

with app.app_context():
    db.create_all()
    if not db.session.execute(db.select(Cafe)).first():
        for name, loc, seats, toilet, wifi, sockets, calls, price in SEED:
            slug = name.lower().replace(" ", "-")
            db.session.add(Cafe(name=name, map_url=f"https://maps.example.com/{slug}",
                                img_url=f"https://img.example.com/{slug}.jpg", location=loc, seats=seats,
                                has_toilet=toilet, has_wifi=wifi, has_sockets=sockets, can_take_calls=calls,
                                coffee_price=price))
        db.session.commit()


def truthy(value: str | None) -> bool:
    return str(value).lower() in {"1", "true", "yes", "on"}


@app.route("/")
def home():
    return render_template_string("<h1>Cafe & Wifi API</h1><p>Endpoints: GET /random, GET /all, GET /search?loc=, "
                                  "POST /add, PATCH /update-price/&lt;id&gt;?new_price=, "
                                  "DELETE /report-closed/&lt;id&gt;?api-key=</p>")


@app.get("/random")
def get_random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafe=random.choice(cafes).to_dict())


@app.get("/all")
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    return jsonify(cafes=[c.to_dict() for c in cafes])


@app.get("/search")
def search():
    loc = request.args.get("loc", "")
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location.ilike(f"%{loc}%"))).scalars().all()
    if not cafes:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    return jsonify(cafes=[c.to_dict() for c in cafes])


@app.post("/add")
def add_cafe():
    f = request.form
    cafe = Cafe(name=f["name"], map_url=f["map_url"], img_url=f["img_url"], location=f["loc"], seats=f["seats"],
                has_toilet=truthy(f.get("toilet")), has_wifi=truthy(f.get("wifi")), has_sockets=truthy(f.get("sockets")),
                can_take_calls=truthy(f.get("calls")), coffee_price=f.get("coffee_price"))
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 201


@app.patch("/update-price/<int:cafe_id>")
def update_price(cafe_id: int):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    cafe.coffee_price = request.args.get("new_price")
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."})


@app.delete("/report-closed/<int:cafe_id>")
def delete_cafe(cafe_id: int):
    key = request.args.get("api-key") or request.headers.get("X-API-Key")
    if key != API_KEY:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key."), 403
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success": "Cafe deleted."})
