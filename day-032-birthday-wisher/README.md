# Day 32: Automated Birthday Wisher

Day 32 - Automated Birthday Wisher: datetime, pandas, random letters, (simulated) email.

API-free: emails are written to a local outbox/ folder instead of being sent via Gmail SMTP.
Run it daily (e.g. cron) to "send" wishes to anyone whose birthday is today.

**Topic:** Email & datetime

**Concepts:** smtplib/email, datetime, pandas, random letters

## Notes

Account-free (replaced Gmail SMTP login with a local outbox/ folder or a local aiosmtpd debug server).

## Files

- `birthdays.csv`
- `main.py`
- `monday_motivation.py`
- `outbox.py`
- `quotes.txt`
- `requirements.txt`

## Run

```bash
pip install -r requirements.txt
python main.py
python monday_motivation.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
