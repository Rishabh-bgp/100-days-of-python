# Day 60: HTML Forms + Flask

Day 60 - HTML forms with Flask: handle POST requests with request.form, a simple
login form, and a contact form that 'emails' the message.

Account-free: the contact form writes to a local outbox/ (or local debug SMTP server via
LOCAL_SMTP=1) instead of logging into Gmail.

Run with:  flask --app app run

**Topic:** POST requests

**Concepts:** forms, request.form, contact form

## Notes

Account-free (contact form emails go to a local outbox).

## Files

- `app.py`
- `outbox.py`
- `requirements.txt`
- `templates/`

## Run

```bash
pip install -r requirements.txt
flask --app app run      # then open http://127.0.0.1:5000
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
