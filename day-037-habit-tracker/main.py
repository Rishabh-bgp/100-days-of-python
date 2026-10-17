"""Day 37 - Habit Tracker: create / read / update / delete records (the HTTP POST, PUT,
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
"""
import random
import sqlite3
import sys
from datetime import date, timedelta
from pathlib import Path

DB = Path(__file__).with_name("habits.db")


def connect(path: Path = DB) -> sqlite3.Connection:
    con = sqlite3.connect(path)
    con.execute("CREATE TABLE IF NOT EXISTS pixels (day TEXT PRIMARY KEY, quantity REAL NOT NULL)")
    return con


def add(con, day: str, qty: float) -> None:
    con.execute("INSERT OR REPLACE INTO pixels VALUES (?, ?)", (day, qty))
    con.commit()


def update(con, day: str, qty: float) -> bool:
    cur = con.execute("UPDATE pixels SET quantity = ? WHERE day = ?", (qty, day))
    con.commit()
    return cur.rowcount == 1


def delete(con, day: str) -> bool:
    cur = con.execute("DELETE FROM pixels WHERE day = ?", (day,))
    con.commit()
    return cur.rowcount == 1


def all_pixels(con) -> list[tuple[str, float]]:
    return con.execute("SELECT day, quantity FROM pixels ORDER BY day").fetchall()


def graph(con, out: Path = Path(__file__).with_name("habit_graph.png"), weeks: int = 26) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    data = dict(all_pixels(con))
    end = date.today()
    start = end - timedelta(days=end.weekday()) - timedelta(weeks=weeks - 1)
    grid = np.full((7, weeks), np.nan)
    for i in range((end - start).days + 1):
        d = start + timedelta(days=i)
        grid[d.weekday(), i // 7] = data.get(d.isoformat(), 0)
    fig, ax = plt.subplots(figsize=(10, 2.6))
    ax.imshow(grid, cmap="Greens", aspect="equal")
    ax.set_yticks(range(7), ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    ax.set_xticks([])
    ax.set_title("Cycling (km) - habit graph")
    fig.tight_layout()
    fig.savefig(out, dpi=120)
    plt.close(fig)
    return out


def main(argv: list[str]) -> None:
    con = connect()
    cmd = argv[0] if argv else "show"
    if cmd == "add":
        add(con, argv[1], float(argv[2]))
    elif cmd == "update":
        print("updated" if update(con, argv[1], float(argv[2])) else "no such day")
    elif cmd == "delete":
        print("deleted" if delete(con, argv[1]) else "no such day")
    elif cmd == "graph":
        print("wrote", graph(con))
    elif cmd == "demo":
        rng = random.Random(37)
        for i in range(120):
            if rng.random() < 0.7:
                add(con, (date.today() - timedelta(days=i)).isoformat(), round(rng.uniform(1, 15), 1))
        print("wrote", graph(con))
    for day, qty in all_pixels(con)[-5:]:
        print(day, qty)


if __name__ == "__main__":
    main(sys.argv[1:])
