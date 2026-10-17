# Day 52: Follower Bot

Day 52 - Follower Bot: open a similar account's followers list, scroll the modal, and
click Follow on everyone (cancelling the 'Unfollow?' dialog for people already followed).

Account-free: the course automates Instagram (real account, against its terms). This drives
'Pictagram', a local mock (mock_site.py) with a fake login. Needs Google Chrome.

**Topic:** Selenium scrolling

**Concepts:** modals, scrolling, handling 'already following'

## Notes

Account-free (replaced Instagram with 'Pictagram', a local Flask mock).

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
