"""'Swipr' - a local mock swiping app with a fake login, cookie banner, location popup and
"It's a match!" overlays, so the bot practises handling popups without a real account.

Run alone:  flask --app mock_site run      Demo login: demo@example.com / demo-password
"""
import random

from flask import Flask, jsonify, redirect, render_template_string, request, session

app = Flask(__name__)
app.secret_key = "local-dev-only"
PROFILES = [f"Sample Person {i}" for i in range(1, 31)]
LIKES: list[str] = []
LIMIT = 20  # free "likes" per day, like the real apps

PAGE = """<!doctype html><html><head><meta charset="utf-8"><title>Swipr</title>
<style>.overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);display:flex;align-items:center;justify-content:center}
.overlay div{background:#fff;padding:20px}</style></head><body>
{% if not session.get('user') %}
<h1>Swipr (local mock)</h1><p>Demo account: demo@example.com / demo-password</p>
<form method="post" action="/login"><input name="email" id="email"><input name="password" id="password" type="password">
<button id="login">Log in</button></form>
{% else %}
<div id="cookies" class="overlay"><div>We use cookies. <button id="accept-cookies" onclick="this.closest('.overlay').remove()">I accept</button></div></div>
<div id="location" class="overlay"><div>Allow location? <button id="allow-location" onclick="this.closest('.overlay').remove()">Allow</button></div></div>
<h2 id="profile-name">...</h2><p id="status"></p>
<button id="nope">Nope</button><button id="like">Like</button>
<script>
async function load(){const r=await fetch('/api/next');const d=await r.json();document.getElementById('profile-name').textContent=d.name||'No more profiles';}
async function like(){const r=await fetch('/api/like',{method:'POST'});const d=await r.json();
 if(d.limit){document.body.insertAdjacentHTML('beforeend','<div id="out-of-likes" class="overlay"><div>Out of likes for today!</div></div>');return;}
 if(d.match){document.body.insertAdjacentHTML('beforeend','<div id="match" class="overlay"><div>It\\'s a match! <a href="#" id="back-to-swiping" onclick="this.closest(\\'.overlay\\').remove();return false">Back to swiping</a></div></div>');}
 load();}
document.getElementById('like').onclick=like;document.getElementById('nope').onclick=()=>{fetch('/api/nope',{method:'POST'}).then(load)};
load();
</script>{% endif %}</body></html>"""

state = {"i": 0, "rng": random.Random(50)}


@app.get("/")
def home():
    return render_template_string(PAGE)


@app.post("/login")
def login():
    if request.form.get("email") == "demo@example.com" and request.form.get("password") == "demo-password":
        session["user"] = "demo"
    return redirect("/")


@app.get("/api/next")
def next_profile():
    i = state["i"]
    return jsonify(name=PROFILES[i] if i < len(PROFILES) else None)


@app.post("/api/like")
def like():
    if len(LIKES) >= LIMIT:
        return jsonify(limit=True)
    LIKES.append(PROFILES[state["i"]])
    state["i"] += 1
    return jsonify(match=state["rng"].random() < 0.25, limit=False)


@app.post("/api/nope")
def nope():
    state["i"] += 1
    return jsonify(ok=True)
