# Day 96: Online Shop

Day 96 - Portfolio project: online shop. Product catalogue, a session-based cart
(add / update quantity / remove), stock checks, and a checkout that creates an order.

Account-free: the course takes payments with Stripe (account + keys). Here checkout is a
MOCK payment step: you enter any name/email and a fake card number; it validates the
format with the Luhn check (try 4242 4242 4242 4242), then records the order in local
SQLite. No money moves and nothing leaves your machine.

Run with:  flask --app app run

**Topic:** Portfolio

**Concepts:** Flask, cart sessions, checkout

## Notes

Account-free (replaced Stripe with a mock local checkout).

## Files

- `app.py`
- `products.json`
- `requirements.txt`
- `templates/`

## Run

```bash
pip install -r requirements.txt
flask --app app run      # then open http://127.0.0.1:5000
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
