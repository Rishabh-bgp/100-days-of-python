# Day 70: Deploying (locally)

Day 70 - Deploying the blog (locally): the Day 69 blog prepared for production -
config from environment variables, a gunicorn server, and an optional Docker image.

Account-free: the course deploys to a hosting provider (account needed). Here you run it
with gunicorn on your own machine, or in Docker; see DEPLOY.md. Below is the Day 69 app:

Users and comments. Register/login (Flask-Login,
hashed passwords), an @admin_only decorator (the first registered user is the admin who
can create, edit and delete posts), relational tables (User 1-many BlogPost/Comment) and
comments on posts.

Users live in this app's own local SQLite db. Gravatar is replaced with local
initials avatars, so no external service is used.

Run with:  flask --app app run

**Topic:** Git & deployment

**Concepts:** gunicorn, env vars, Docker

## Notes

Account-free (replaced Heroku/Render hosting with local gunicorn + optional Docker).

## Files

- `.dockerignore`
- `.env.example`
- `DEPLOY.md`
- `Dockerfile`
- `app.py`
- `gunicorn.conf.py`
- `requirements.txt`
- `templates/`

## Run

```bash
pip install -r requirements.txt
flask --app app run      # then open http://127.0.0.1:5000
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
