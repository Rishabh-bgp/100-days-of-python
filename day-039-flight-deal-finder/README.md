# Day 39: Flight Deal Finder

Day 39 - Flight Deal Finder: classes working together (DataManager, FlightSearch,
NotificationManager) to find flights cheaper than your target price.

API-free / account-free: replaces the Google Sheet (Sheety), the flight-search API
(Tequila/Kiwi, now closed; later Amadeus) and Twilio SMS with destinations.csv,
sample_flights.csv (synthetic prices) and a local outbox. The search falls back to
1-stop flights when there's no direct one, as in the course's later version.

**Topic:** Classes working together

**Concepts:** multi-module OOP, dataclasses, searching data

## Notes

API-free (replaced Sheety, Tequila/Kiwi (shut down) and Twilio with local CSVs, synthetic flight data and outbox).

## Files

- `data_manager.py`
- `destinations.csv`
- `flight_search.py`
- `main.py`
- `outbox.py`
- `sample_flights.csv`

## Run

```bash
python main.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
