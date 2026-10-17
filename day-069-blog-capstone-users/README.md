# Day 69: Blog Capstone pt 4

Day 69 - Blog Capstone part 4: users and comments. Register/login (Flask-Login,
hashed passwords), an @admin_only decorator (the first registered user is the admin who
can create, edit and delete posts), relational tables (User 1-many BlogPost/Comment) and
comments on posts.

Users live in this app's own local SQLite db. Gravatar is replaced with local
initials avatars, so no external service is used.

Run with:  flask --app app run

**Topic:** Users & comments

**Concepts:** relationships, admin-only decorator, comments

## Notes

Local SQLite users; Gravatar replaced by local initials avatars.

## Files

- `app.py`
- `requirements.txt`
- `templates/`

## Run

```bash
pip install -r requirements.txt
flask --app app run      # then open http://127.0.0.1:5000
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
