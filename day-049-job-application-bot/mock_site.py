"""'MockedIn' - a tiny local job board with a fake login, so the bot needs no real account.

Run on its own with:  flask --app mock_site run   (then open http://127.0.0.1:5000)
Demo login: demo@example.com / demo-password
"""
from flask import Flask, redirect, render_template_string, request, session, url_for

app = Flask(__name__)
app.secret_key = "local-dev-only"
USER = {"email": "demo@example.com", "password": "demo-password"}
JOBS = [
    {"id": 1, "title": "Junior Python Developer", "company": "Sample Labs", "easy": True},
    {"id": 2, "title": "Data Analyst (Python)", "company": "Mock Metrics", "easy": True},
    {"id": 3, "title": "Backend Engineer", "company": "Demo Corp", "easy": False},
    {"id": 4, "title": "ML Intern", "company": "Placeholder AI", "easy": True},
    {"id": 5, "title": "Automation Tester", "company": "Fixture Systems", "easy": True},
]
APPLICATIONS: list[dict] = []
SAVED: set[int] = set()

BASE = """<!doctype html><html><head><meta charset="utf-8"><title>MockedIn</title></head><body>
<header><b>MockedIn</b> (local mock site) {% if session.get('user') %}| <a id="logout" href="/logout">Log out</a>{% endif %}</header>
{% block body %}{% endblock %}</body></html>"""

LOGIN = BASE.replace("{% block body %}{% endblock %}", """
<h1>Sign in</h1><p>Demo account: demo@example.com / demo-password</p>
{% if error %}<p id="error">{{ error }}</p>{% endif %}
<form method="post"><input id="username" name="email" placeholder="Email">
<input id="password" name="password" type="password" placeholder="Password">
<button id="sign-in" type="submit">Sign in</button></form>""")

JOBS_PAGE = BASE.replace("{% block body %}{% endblock %}", """
<h1>Python jobs</h1><ul id="job-list">{% for j in jobs %}
<li class="job-card" data-id="{{ j.id }}"><a class="job-link" href="/jobs/{{ j.id }}">{{ j.title }}</a> - {{ j.company }}
{% if j.easy %}<span class="easy-apply-tag">Easy Apply</span>{% endif %}</li>{% endfor %}</ul>""")

JOB_PAGE = BASE.replace("{% block body %}{% endblock %}", """
<h1 id="job-title">{{ job.title }}</h1><p>{{ job.company }}</p>
<form method="post" action="/jobs/{{ job.id }}/save"><button class="save-btn">{{ 'Saved' if job.id in saved else 'Save' }}</button></form>
{% if applied %}<p id="applied">Application submitted</p>
{% elif job.easy %}<form method="post" action="/jobs/{{ job.id }}/apply" id="apply-form">
<label>Mobile phone <input id="phone" name="phone"></label><button id="submit-application">Submit application</button></form>
{% else %}<p id="multi-step">This job requires a multi-step application on the company site.</p>{% endif %}
<a href="/jobs" id="back">Back to jobs</a>""")


def logged_in() -> bool:
    return session.get("user") == USER["email"]


@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form.get("email") == USER["email"] and request.form.get("password") == USER["password"]:
            session["user"] = USER["email"]
            return redirect(url_for("jobs"))
        error = "Wrong email or password"
    return render_template_string(LOGIN, error=error)


@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.get("/jobs")
def jobs():
    if not logged_in():
        return redirect(url_for("login"))
    return render_template_string(JOBS_PAGE, jobs=JOBS)


@app.get("/jobs/<int:job_id>")
def job(job_id: int):
    if not logged_in():
        return redirect(url_for("login"))
    j = next(j for j in JOBS if j["id"] == job_id)
    applied = any(a["job_id"] == job_id for a in APPLICATIONS)
    return render_template_string(JOB_PAGE, job=j, applied=applied, saved=SAVED)


@app.post("/jobs/<int:job_id>/save")
def save(job_id: int):
    SAVED.add(job_id)
    return redirect(url_for("job", job_id=job_id))


@app.post("/jobs/<int:job_id>/apply")
def apply(job_id: int):
    if not logged_in():
        return redirect(url_for("login"))
    APPLICATIONS.append({"job_id": job_id, "phone": request.form.get("phone", "")})
    return redirect(url_for("job", job_id=job_id))
