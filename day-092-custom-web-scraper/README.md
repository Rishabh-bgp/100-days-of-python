# Day 92: Custom Web Scraper

Day 92 - Portfolio project: custom web scraper. Crawl a paginated product listing,
extract title, price, star rating and stock, follow 'next' links, and export to CSV.

Offline: crawls the bundled sample_site/ (a fictional bookshop) by following local links,
so it never hits a real site. The same code works on a URL if you swap in a fetch function.

  python main.py                     # writes output/books.csv

**Topic:** Portfolio

**Concepts:** BeautifulSoup, CSV export

## Notes

Offline (bundled sample site).

## Files

- `main.py`
- `requirements.txt`
- `sample_site/`

## Run

```bash
pip install -r requirements.txt
python main.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
