# Day 53: Data Entry Automation

Day 53 - Data Entry Job Automation capstone: scrape rental listings with BeautifulSoup,
then use Selenium to type each one into a form, building a spreadsheet of results.

Account-free/offline: the course scrapes a Zillow clone and fills a Google Form (Google
account). This scrapes the bundled listings.html and fills a local Flask form
(form_site.py) that appends to responses.csv. Needs Google Chrome.

**Topic:** Capstone: scrape + automate

**Concepts:** BeautifulSoup + Selenium form filling, CSV

## Notes

Account-free (replaced Zillow clone + Google Forms with bundled listings HTML and a local Flask form that saves to CSV).

This is a Selenium bot. It needs Google Chrome installed (Selenium Manager fetches the matching driver automatically). It starts a bundled local mock site on 127.0.0.1 and only talks to that, so no real account or website is involved. Set `HEADLESS=0` to watch it.

## Files

- `browser.py`
- `form_site.py`
- `listings.html`
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
