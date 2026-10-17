# Day 67: Blog Capstone pt 3

Day 67 - Blog Capstone part 3: a RESTful blog with full CRUD (create, read, update,
delete) on SQLite via Flask-SQLAlchemy 3.1, using WTForms 3 + Bootstrap-Flask.

The course uses Flask-CKEditor for rich text; this uses a plain textarea whose text is
rendered with line breaks (no extra dependency).

Run with:  flask --app app run

**Topic:** RESTful blog

**Concepts:** CRUD routes, forms, rich text

## Notes

A plain textarea replaces Flask-CKEditor.

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
