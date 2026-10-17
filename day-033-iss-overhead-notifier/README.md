# Day 33: ISS Overhead Notifier

Day 33 - ISS Overhead Notifier: "API" logic, datetimes, and a notification when the ISS
is overhead and it's dark.

API-free: ISS position and sunrise/sunset are computed offline in astro.py
(replacing the Open Notify and sunrise-sunset.org APIs); the alert is printed/written
to outbox.txt instead of emailed.

**Topic:** APIs (offline)

**Concepts:** API-shaped data, datetime, maths, notifications

## Notes

API-free (replaced Open Notify + sunrise-sunset.org with offline orbit and NOAA solar formulas; Kanye API with bundled quotes; email with local outbox).

## Files

- `astro.py`
- `kanye_quotes.json`
- `main.py`
- `quote_app.py`

## Run

```bash
python main.py
python quote_app.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
