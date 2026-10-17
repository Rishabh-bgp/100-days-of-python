# Day 36: Stock News Alert

Day 36 - Stock Trading News Alert: compare yesterday vs the day before; if the move is
over 5%, send the top 3 news headlines.

API-free / account-free: replaces Alpha Vantage (prices), NewsAPI (news) and Twilio (SMS)
with bundled sample_daily_prices.csv, sample_news.json (fictional company) and a local outbox.

**Topic:** Capstone: APIs (offline)

**Concepts:** CSV parsing, percentage change, slicing, alerts

## Notes

API-free (replaced Alpha Vantage, NewsAPI and Twilio with bundled sample prices/news and local outbox).

## Files

- `main.py`
- `outbox.py`
- `sample_daily_prices.csv`
- `sample_news.json`

## Run

```bash
python main.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
