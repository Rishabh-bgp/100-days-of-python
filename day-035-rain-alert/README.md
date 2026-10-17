# Day 35: Rain Alert

Day 35 - Rain Alert: reading JSON "API responses", nested data, and sending an alert.

API-free / account-free: the course calls OpenWeather (API key) and sends SMS via Twilio
(account). Here the forecast is a bundled sample_forecast.json with the same structure as
OpenWeather's 3-hourly forecast, and the "SMS" goes to the console + local outbox/.

**Topic:** API keys & SMS (offline)

**Concepts:** nested JSON, weather codes, notifications

## Notes

API-free (replaced OpenWeather with a bundled sample forecast; Twilio SMS with local outbox).

## Files

- `main.py`
- `outbox.py`
- `sample_forecast.json`
- `sample_forecast_dry.json`

## Run

```bash
python main.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
