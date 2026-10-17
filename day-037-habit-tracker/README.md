# Day 37: Habit Tracker

Day 37 - Habit Tracker: create / read / update / delete records (the HTTP POST, PUT,
DELETE ideas) and draw a GitHub-style contribution graph.

API-free / account-free: the course stores data on Pixela (account + token). Here a local
SQLite database plays the "server" and matplotlib draws the graph to habit_graph.png.

Usage:
  python main.py add 2026-10-18 5.2      # POST   - add today's value
  python main.py update 2026-10-18 6.0   # PUT    - change a value
  python main.py delete 2026-10-18       # DELETE - remove a value
  python main.py show                     # GET    - list values
  python main.py graph                    # draw habit_graph.png
  python main.py demo                     # fill 120 days of sample data and draw it

**Topic:** HTTP verbs (offline)

**Concepts:** create/read/update/delete, SQLite, matplotlib heatmap

## Notes

API-free (replaced Pixela account + token with local SQLite and a matplotlib graph).

## Files

- `main.py`
- `requirements.txt`

## Run

```bash
pip install -r requirements.txt
python main.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
