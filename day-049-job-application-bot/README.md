# Day 49: Job Application Bot

Day 49 - Automated job application bot (Selenium): log in, open each job, save it, and
submit the "Easy Apply" ones that only need a phone number; skip multi-step applications.

Account-free: the course automates LinkedIn (real account, against its terms). This bot
drives 'MockedIn', a local Flask mock (mock_site.py) with a fake login, started on
127.0.0.1 automatically. Needs Google Chrome. HEADLESS=0 to watch.

**Topic:** Selenium automation

**Concepts:** logins, navigation, explicit waits, skipping cases

## Notes

Account-free (replaced LinkedIn with 'MockedIn', a local Flask mock with a fake login).

This is a Selenium bot. It needs Google Chrome installed (Selenium Manager fetches the matching driver automatically). It starts a bundled local mock site on 127.0.0.1 and only talks to that, so no real account or website is involved. Set `HEADLESS=0` to watch it.

## Files

- `browser.py`
- `local_server.py`
- `main.py`
- `mock_site.py`
- `requirements.txt`

## Run

```bash
pip install -r requirements.txt
python main.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
