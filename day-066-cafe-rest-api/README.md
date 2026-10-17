# Day 66: Cafe REST API

Day 66 - Build your own RESTful API: a cafe database with GET (random, all, search),
POST (add), PATCH (update price) and DELETE (report closed, needs an API key header/param).

This is YOUR local API, so its 'API key' is just a local demo value you choose
(env CAFE_API_KEY, default 'TopSecretAPIKey'); no external service is involved.
Seeded with a few fictional cafes on first run.

Run with:  flask --app app run   then try  curl http://127.0.0.1:5000/random

**Topic:** Build a REST API

**Concepts:** GET/POST/PATCH/DELETE, JSON, API key header

## Notes

The API key is a local demo value checked by your own app.

## Files

- `API_DOCS.md`
- `app.py`
- `requirements.txt`

## Run

```bash
pip install -r requirements.txt
flask --app app run      # then open http://127.0.0.1:5000
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
