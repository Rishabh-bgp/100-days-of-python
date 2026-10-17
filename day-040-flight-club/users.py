"""Flight Club members stored in local SQLite (instead of a Google Form + Sheety 'users' sheet)."""
import re
import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("flight_club.db")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def connect(path: Path = DB) -> sqlite3.Connection:
    con = sqlite3.connect(path)
    con.execute("CREATE TABLE IF NOT EXISTS users (first TEXT, last TEXT, email TEXT UNIQUE)")
    return con


def add_user(con, first: str, last: str, email: str) -> bool:
    if not EMAIL_RE.match(email):
        return False
    con.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?)", (first, last, email.lower()))
    con.commit()
    return True


def emails(con) -> list[str]:
    return [r[0] for r in con.execute("SELECT email FROM users")]
