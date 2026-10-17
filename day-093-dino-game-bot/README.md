# Day 93: Dino Game Bot

Day 93 - Portfolio project: bot that plays a dinosaur runner game by itself.
Selenium reads the obstacle positions from the page and presses Space just in time.

Offline: the course targets Chrome's built-in dino game / an online copy. This plays the
bundled dino.html (a small runner written for this repo) served on 127.0.0.1.
Needs Google Chrome. Set HEADLESS=0 to watch; RUN_SECONDS to change how long it plays.

**Topic:** Portfolio

**Concepts:** Selenium, game automation

## Notes

Offline (local dino-runner page).

This is a Selenium bot. It needs Google Chrome installed (Selenium Manager fetches the matching driver automatically). It starts a bundled local mock site on 127.0.0.1 and only talks to that, so no real account or website is involved. Set `HEADLESS=0` to watch it.

## Files

- `browser.py`
- `dino.html`
- `local_server.py`
- `main.py`
- `requirements.txt`

## Run

```bash
pip install -r requirements.txt
python main.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
