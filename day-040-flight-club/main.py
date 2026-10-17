"""Day 40 - Flight Club: sign members up, then email every member when there's a deal.

Account-free: members live in a local SQLite db (not a Google Sheet/Form), and emails go
to a local outbox/ or local debug SMTP server (not Gmail).

  python main.py signup     # interactive sign-up (asks for name + email twice)
  python main.py deals      # check deals and email all members
"""
import sys
from datetime import date, timedelta

import users
from data_manager import get_destinations
from flight_search import FlightSearch
from outbox import send_email


def signup(ask=input) -> bool:
    print("Welcome to Rishabh's Flight Club.\nWe find the best flight deals and email you.")
    first = ask("What is your first name?\n> ")
    last = ask("What is your last name?\n> ")
    email = ask("What is your email?\n> ")
    if ask("Type your email again.\n> ") != email:
        print("Emails don't match.")
        return False
    ok = users.add_user(users.connect(), first, last, email)
    print("You're in the club!" if ok else "That doesn't look like an email address.")
    return ok


def deals(today: date = date(2026, 11, 1)) -> int:
    search, members = FlightSearch(), users.emails(users.connect())
    sent = 0
    for dest in get_destinations():
        f = search.cheapest("DEL", dest["iata"], today, today + timedelta(days=180), max_stops=1)
        if f and f.price < dest["lowest_price_inr"]:
            for m in members:
                send_email(m, f"New low price flight to {dest['city']}!",
                           f"Only ₹{f.price:,} from {f.origin} to {f.destination}, {f.out_date} to {f.return_date}, "
                           f"{f.stops} stop(s).")
                sent += 1
    print(f"Sent {sent} email(s) to {len(members)} member(s).")
    return sent


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "deals"
    signup() if cmd == "signup" else deals()
