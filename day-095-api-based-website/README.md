# Day 95: Custom API-based Website

Day 95 - Portfolio project: an API-based website. The page is a small single-page app
that fetches JSON from an API and renders it (random quote, search by tag, list all).

API-free in the sense of 'no external service': the API is served by this same Flask app
from bundled quotes.json, so the whole thing runs offline with no key.

Run with:  flask --app app run    API:  /api/quotes, /api/quotes/random, /api/quotes?tag=python

**Topic:** Portfolio

**Concepts:** Flask, JSON API, fetch

## Notes

API-free (the site serves and consumes its own local JSON API).

## Files

- `app.py`
- `quotes.json`
- `requirements.txt`
- `templates/`

## Run

```bash
pip install -r requirements.txt
flask --app app run      # then open http://127.0.0.1:5000
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
