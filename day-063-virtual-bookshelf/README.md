# Day 63: Virtual Bookshelf

Day 63 - Virtual Bookshelf: SQLite with Flask-SQLAlchemy 3.1 and SQLAlchemy 2.0 style
(typed Mapped models, db.select, db.session.get, app context). Add, edit rating, delete.

Run with:  flask --app app run      (creates instance/books.db on first run)

**Topic:** SQLite + SQLAlchemy

**Concepts:** Flask-SQLAlchemy 3.1, CRUD, db.session.get

## Notes

SQLAlchemy 2.0-style queries.

## Files

- `app.py`
- `requirements.txt`
- `sqlite_basics.py`
- `templates/`

## Run

```bash
pip install -r requirements.txt
flask --app app run      # then open http://127.0.0.1:5000
python sqlite_basics.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
