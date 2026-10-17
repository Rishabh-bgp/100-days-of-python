"""Day 38 - Workout Tracker: turn "ran 5 km and did yoga for 20 minutes" into rows with
calories, and log them with date and time.

API-free / account-free: the course uses Nutritionix's natural-language API (key) and a
Google Sheet via Sheety (account). Here a small local parser + MET table
(exercises_met.csv, standard MET-style values) estimates calories, and rows go to a
local SQLite database (workouts.db) plus workouts.csv.
"""
import csv
import re
import sqlite3
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
WEIGHT_KG = 70.0
KMH = {"Running": 10.0, "Jogging": 8.0, "Walking": 5.0, "Cycling": 18.0, "Hiking": 4.0, "Swimming": 2.5}


def load_table() -> list[dict]:
    with open(HERE / "exercises_met.csv", newline="") as fh:
        return list(csv.DictReader(fh))


def parse(text: str, weight_kg: float = WEIGHT_KG) -> list[dict]:
    table = load_table()
    results = []
    for part in re.split(r",| and |;|\bthen\b", text.lower()):
        row = next((r for r in table if r["keyword"] in part), None)
        if not row:
            continue
        minutes = float(row["default_minutes"])
        if m := re.search(r"(\d+(?:\.\d+)?)\s*(?:min|minutes|mins)", part):
            minutes = float(m.group(1))
        elif m := re.search(r"(\d+(?:\.\d+)?)\s*(km|kilomet|mile)", part):
            km = float(m.group(1)) * (1.609 if m.group(2) == "mile" else 1)
            minutes = round(km / KMH.get(row["exercise"], 6.0) * 60)
        elif m := re.search(r"(\d+(?:\.\d+)?)\s*(?:h|hour|hours|hr)", part):
            minutes = float(m.group(1)) * 60
        calories = float(row["met"]) * 3.5 * weight_kg / 200 * minutes
        results.append({"exercise": row["exercise"], "duration": round(minutes), "calories": round(calories)})
    return results


def save(rows: list[dict], db: Path = HERE / "workouts.db", csv_path: Path = HERE / "workouts.csv") -> None:
    now = datetime.now()
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE IF NOT EXISTS workouts (date TEXT, time TEXT, exercise TEXT, duration INT, calories INT)")
    new_file = not csv_path.exists()
    with open(csv_path, "a", newline="") as fh:
        w = csv.writer(fh)
        if new_file:
            w.writerow(["Date", "Time", "Exercise", "Duration", "Calories"])
        for r in rows:
            vals = (now.strftime("%d/%m/%Y"), now.strftime("%X"), r["exercise"].title(), r["duration"], r["calories"])
            con.execute("INSERT INTO workouts VALUES (?, ?, ?, ?, ?)", vals)
            w.writerow(vals)
    con.commit()
    con.close()


if __name__ == "__main__":
    text = input("Tell me which exercises you did: ")
    rows = parse(text)
    for r in rows:
        print(f"{r['exercise']}: {r['duration']} min, ~{r['calories']} kcal")
    if rows:
        save(rows)
        print("Saved to workouts.db and workouts.csv")
    else:
        print("Sorry, I didn't recognise any exercise.")
