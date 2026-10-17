# Day 68: Flask Authentication

Day 68 - Authentication with Flask: register, log in and log out with Flask-Login;
passwords hashed and salted with Werkzeug (pbkdf2/scrypt); flash messages; a protected
page and file download.

Users register in this app's own local SQLite database - no external account needed.

Run with:  flask --app app run

**Topic:** Auth

**Concepts:** Flask-Login, password hashing, flash messages

## Notes

Users register in the app's own local SQLite (no external account).

## Files

- `app.py`
- `requirements.txt`
- `static/`
- `templates/`

## Run

```bash
pip install -r requirements.txt
flask --app app run      # then open http://127.0.0.1:5000
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
