"""'Pictagram' - a local mock photo site: fake login, an account page with a scrollable
followers modal, Follow buttons, and an 'Unfollow?' dialog for people you already follow.

Run alone:  flask --app mock_site run      Demo login: demo@example.com / demo-password
"""
from flask import Flask, jsonify, redirect, render_template_string, request, session

app = Flask(__name__)
app.secret_key = "local-dev-only"
FOLLOWERS = [f"sample_user_{i:02d}" for i in range(1, 41)]
FOLLOWING: set[str] = {"sample_user_03", "sample_user_10"}

PAGE = """<!doctype html><html><head><meta charset="utf-8"><title>Pictagram</title>
<style>#modal{position:fixed;top:10%;left:30%;width:40%;height:60%;background:#fff;border:1px solid #999}
#modal-list{height:85%;overflow-y:scroll}.row{height:48px}#confirm{position:fixed;top:40%;left:40%;background:#eee;padding:20px;border:1px solid #333}</style></head><body>
{% if not session.get('user') %}<h1>Pictagram (local mock)</h1><p>Demo account: demo@example.com / demo-password</p>
<form method="post" action="/login"><input id="email" name="email"><input id="password" name="password" type="password"><button id="login">Log in</button></form>
{% else %}<h1>@chefsample</h1><a href="#" id="followers-link">{{ followers|length }} followers</a>
<div id="modal" hidden><button id="close">x</button><div id="modal-list">
{% for f in followers %}<div class="row"><span>{{ f }}</span>
<button class="follow-btn" data-user="{{ f }}">{{ 'Following' if f in following else 'Follow' }}</button></div>{% endfor %}
</div></div>
<script>
document.getElementById('followers-link').onclick=e=>{e.preventDefault();document.getElementById('modal').hidden=false;};
document.querySelectorAll('.follow-btn').forEach(b=>b.onclick=async()=>{
 if(b.textContent==='Following'){document.body.insertAdjacentHTML('beforeend','<div id="confirm">Unfollow '+b.dataset.user+'? <button id="cancel">Cancel</button></div>');
  document.getElementById('cancel').onclick=()=>document.getElementById('confirm').remove();return;}
 await fetch('/api/follow/'+b.dataset.user,{method:'POST'});b.textContent='Following';});
</script>{% endif %}</body></html>"""


@app.get("/")
def home():
    return render_template_string(PAGE, followers=FOLLOWERS, following=FOLLOWING)


@app.post("/login")
def login():
    if request.form.get("email") == "demo@example.com" and request.form.get("password") == "demo-password":
        session["user"] = "demo"
    return redirect("/")


@app.post("/api/follow/<user>")
def follow(user: str):
    FOLLOWING.add(user)
    return jsonify(following=len(FOLLOWING))
