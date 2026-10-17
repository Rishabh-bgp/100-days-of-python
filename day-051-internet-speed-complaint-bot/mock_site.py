"""Two local mock sites in one Flask app, so the bot needs no real account:
  /speed  - a fake speed-test page (numbers are random, after a short "test")
  /chirp  - 'Chirp', a fake social site with a login and a post box

Run alone:  flask --app mock_site run      Demo login: demo@example.com / demo-password
"""
from flask import Flask, redirect, render_template_string, request, session

app = Flask(__name__)
app.secret_key = "local-dev-only"
POSTS: list[str] = []

SPEED = """<!doctype html><html><head><meta charset="utf-8"><title>Local Speed Test</title></head><body>
<h1>Speed test (mock)</h1><button id="go">GO</button><p id="status"></p>
<p>Download: <span id="download-speed">--</span> Mbps</p><p>Upload: <span id="upload-speed">--</span> Mbps</p>
<script>
document.getElementById('go').onclick=()=>{document.getElementById('status').textContent='Testing...';
setTimeout(()=>{document.getElementById('download-speed').textContent=(20+Math.random()*60).toFixed(2);
document.getElementById('upload-speed').textContent=(2+Math.random()*10).toFixed(2);
document.getElementById('status').textContent='Done';},1500);};
</script></body></html>"""

CHIRP = """<!doctype html><html><head><meta charset="utf-8"><title>Chirp</title></head><body>
<h1>Chirp (local mock)</h1>
{% if not session.get('user') %}<p>Demo account: demo@example.com / demo-password</p>
<form method="post" action="/chirp/login"><input id="email" name="email"><input id="password" name="password" type="password">
<button id="login">Log in</button></form>
{% else %}<form method="post" action="/chirp/post"><textarea id="compose" name="text" maxlength="280"></textarea>
<button id="post">Post</button></form>
<ul id="timeline">{% for p in posts|reverse %}<li class="post">{{ p }}</li>{% endfor %}</ul>{% endif %}
</body></html>"""


@app.get("/speed")
def speed():
    return SPEED


@app.get("/chirp")
def chirp():
    return render_template_string(CHIRP, posts=POSTS)


@app.post("/chirp/login")
def login():
    if request.form.get("email") == "demo@example.com" and request.form.get("password") == "demo-password":
        session["user"] = "demo"
    return redirect("/chirp")


@app.post("/chirp/post")
def post():
    if session.get("user") and request.form.get("text"):
        POSTS.append(request.form["text"][:280])
    return redirect("/chirp")
