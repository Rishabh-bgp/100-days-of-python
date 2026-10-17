# Day 51: Internet Speed Complaint Bot

Day 51 - Internet Speed Complaint Bot: a class that runs a speed test with Selenium and,
if the result is below what you pay for, posts a complaint.

Account-free: the course uses speedtest.net and Twitter/X (account; the X API is now paid).
This drives a local mock speed page and 'Chirp', a local mock social site with a fake login
(mock_site.py). Needs Google Chrome. HEADLESS=0 to watch.

**Topic:** Selenium + classes

**Concepts:** waiting for results, posting to a site, classes

## Notes

Account-free (replaced speedtest.net + Twitter/X with a local mock speed page and 'Chirp' mock social site).

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
