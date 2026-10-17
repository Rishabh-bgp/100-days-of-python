# Day 38: Workout Tracker

Day 38 - Workout Tracker: turn "ran 5 km and did yoga for 20 minutes" into rows with
calories, and log them with date and time.

API-free / account-free: the course uses Nutritionix's natural-language API (key) and a
Google Sheet via Sheety (account). Here a small local parser + MET table
(exercises_met.csv, standard MET-style values) estimates calories, and rows go to a
local SQLite database (workouts.db) plus workouts.csv.

**Topic:** NLP & sheets (offline)

**Concepts:** regex parsing, MET calorie maths, SQLite/CSV

## Notes

API-free (replaced Nutritionix with a local MET table parser; Google Sheets/Sheety with SQLite + CSV).

## Files

- `exercises_met.csv`
- `main.py`
- `workouts.csv`
- `workouts.db`

## Run

```bash
python main.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
