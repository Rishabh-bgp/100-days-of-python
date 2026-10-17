# Day 47: Price Tracker

Day 47 - Price Tracker: scrape a product price and send an alert if it's below your target.

Account-free/offline: the course scrapes Amazon (which blocks bots and needs headers) and
emails via Gmail SMTP. Here it parses the bundled product_page.html (or any saved page you
pass) and the alert goes to a local outbox / local debug SMTP server.

**Topic:** Scraping + alerts

**Concepts:** selectors with fallbacks, regex price parsing, alerts

## Notes

Account-free (replaced live Amazon scraping + Gmail with a bundled product page and local outbox).

## Files

- `main.py`
- `outbox.py`
- `product_page.html`
- `requirements.txt`

## Run

```bash
pip install -r requirements.txt
python main.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
