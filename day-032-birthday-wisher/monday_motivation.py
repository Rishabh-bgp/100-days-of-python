"""Day 32 exercise: on Mondays, 'email' a random motivational quote (to the local outbox)."""
import random
import sys
from datetime import date
from pathlib import Path

from outbox import send_email


def main(today: date | None = None, force: bool = False) -> bool:
    today = today or date.today()
    if today.weekday() != 0 and not force:
        print("Not Monday - no quote today. (Use --force to send anyway.)")
        return False
    quote = random.choice(Path(__file__).with_name("quotes.txt").read_text().splitlines())
    send_email("me@example.com", "Monday Motivation", quote)
    return True


if __name__ == "__main__":
    main(force="--force" in sys.argv)
