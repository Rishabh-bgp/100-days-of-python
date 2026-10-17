# Day 50: Auto-Swipe Bot

Day 50 - Auto-swiping bot (Selenium): log in, dismiss the cookie and location popups,
press Like repeatedly, close "It's a match!" overlays, and stop at the daily like limit.

Account-free: the course automates Tinder (real account). This drives 'Swipr', a local mock
(mock_site.py) with a fake login. Needs Google Chrome. HEADLESS=0 to watch.

**Topic:** Selenium popups

**Concepts:** handling overlays/popups, exceptions, limits

## Notes

Account-free (replaced Tinder with 'Swipr', a local Flask mock).

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
