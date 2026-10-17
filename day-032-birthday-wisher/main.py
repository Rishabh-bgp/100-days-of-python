"""Day 32 - Automated Birthday Wisher: datetime, pandas, random letters, (simulated) email.

API-free: emails are written to a local outbox/ folder instead of being sent via Gmail SMTP.
Run it daily (e.g. cron) to "send" wishes to anyone whose birthday is today.
"""
import random
import sys
from datetime import date
from pathlib import Path

import pandas as pd

from outbox import send_email

HERE = Path(__file__).parent


def todays_birthdays(today: date, csv_path: Path = HERE / "birthdays.csv") -> list[dict]:
    df = pd.read_csv(csv_path)
    hits = df[(df["month"] == today.month) & (df["day"] == today.day)]
    return hits.to_dict(orient="records")


def letter_for(name: str, rng=random) -> str:
    template = rng.choice(sorted((HERE / "letter_templates").glob("letter_*.txt")))
    return template.read_text(encoding="utf-8").replace("[NAME]", name)


def main(today: date | None = None) -> int:
    today = today or date.today()
    people = todays_birthdays(today)
    for person in people:
        send_email(person["email"], "Happy Birthday!", letter_for(person["name"]))
    print(f"{len(people)} birthday email(s) written to outbox/ for {today}.")
    return len(people)


if __name__ == "__main__":
    main(date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else None)
