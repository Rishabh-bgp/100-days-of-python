# Day 40: Flight Club

Day 40 - Flight Club: sign members up, then email every member when there's a deal.

Account-free: members live in a local SQLite db (not a Google Sheet/Form), and emails go
to a local outbox/ or local debug SMTP server (not Gmail).

  python main.py signup     # interactive sign-up (asks for name + email twice)
  python main.py deals      # check deals and email all members

**Topic:** Capstone: users

**Concepts:** SQLite users, input validation, bulk notifications

## Notes

Account-free (replaced Google Form/Sheet with local SQLite; Gmail with local outbox).

## Files

- `data_manager.py`
- `destinations.csv`
- `flight_club.db`
- `flight_search.py`
- `main.py`
- `outbox.py`
- `sample_flights.csv`
- `users.py`

## Run

```bash
python main.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
