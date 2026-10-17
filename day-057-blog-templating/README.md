# Day 57: Blog Templating

Day 57 - Templating with Jinja: expressions, for loops, if statements, url_for, and
rendering a blog from JSON data.

API-free: the course fetches blog posts from npoint.io and guesses age/gender via the
agify/genderize APIs. Here posts come from bundled posts.json, and /guess/<name> uses a
small deterministic local function (just for practising templates - it's not a real guess).

Run with:  flask --app app run

**Topic:** Jinja

**Concepts:** Jinja expressions, loops, URL building

## Notes

API-free (replaced agify/genderize/npoint APIs with bundled JSON and a local guess function).

## Files

- `app.py`
- `posts.json`
- `requirements.txt`
- `templates/`

## Run

```bash
pip install -r requirements.txt
flask --app app run      # then open http://127.0.0.1:5000
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
