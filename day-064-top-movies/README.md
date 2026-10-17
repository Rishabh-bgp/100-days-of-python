# Day 64: Top 10 Movies

Day 64 - My Top 10 Movies: Flask + SQLAlchemy CRUD with WTForms, ranking movies by
rating, and a two-step 'search then select' add flow.

API-free: the course searches TMDB (API key) for movie details and posters. Here the
search runs over a bundled catalogue.json (titles, years, short original descriptions),
and posters are drawn as coloured placeholders.

Run with:  flask --app app run

**Topic:** SQLAlchemy + forms

**Concepts:** CRUD, ranking, forms

## Notes

API-free (replaced TMDB search with a bundled movie catalogue).

## Files

- `app.py`
- `catalogue.json`
- `requirements.txt`
- `templates/`

## Run

```bash
pip install -r requirements.txt
flask --app app run      # then open http://127.0.0.1:5000
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
