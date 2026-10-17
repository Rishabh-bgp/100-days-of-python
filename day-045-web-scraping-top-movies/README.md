# Day 45: Top Movies Scraper

Day 45 - Web scraping with BeautifulSoup: extract the movie list and save it in order.

Offline: scrapes the bundled sample_pages/top_movies.html (written for this repo) instead
of a live website, so it always works. Selectors have fallbacks in case the markup changes;
point SOURCE at another file or pass a URL-downloaded HTML file to try your own.

**Topic:** BeautifulSoup

**Concepts:** parsing HTML, CSS selectors, fallbacks, writing files

## Notes

Offline (scrapes bundled sample HTML; selectors have fallbacks).

## Files

- `exercises.py`
- `main.py`
- `movies.txt`
- `requirements.txt`

## Run

```bash
pip install -r requirements.txt
python main.py
python exercises.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
