# Day 48: Cookie Clicker Bot

Day 48 - Selenium Cookie Clicker bot: click the cookie non-stop and, every 5 seconds,
buy the most expensive upgrade you can afford. Stops after RUN_SECONDS and prints the rate.

Offline: drives the bundled cookie.html (a small cookie-clicker written for this repo)
served from 127.0.0.1, not the real orteil.dashnet.org game. Needs Google Chrome installed.
Selenium 4 style: By locators + Selenium Manager (no chromedriver path).

**Topic:** Selenium

**Concepts:** Selenium 4 By locators, clicks, timing, forms

## Notes

Offline (drives a bundled local cookie-clicker page).

This is a Selenium bot. It needs Google Chrome installed (Selenium Manager fetches the matching driver automatically). It starts a bundled local mock site on 127.0.0.1 and only talks to that, so no real account or website is involved. Set `HEADLESS=0` to watch it.

## Files

- `browser.py`
- `cookie.html`
- `events.html`
- `exercises.py`
- `local_server.py`
- `main.py`
- `requirements.txt`

## Run

```bash
pip install -r requirements.txt
python main.py
python exercises.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
