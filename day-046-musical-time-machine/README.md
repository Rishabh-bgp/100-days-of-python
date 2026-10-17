# Day 46: Musical Time Machine

Day 46 - Musical Time Machine: pick a date, scrape that week's top 100 songs, make a playlist.

Account-free: the course scrapes Billboard and creates a Spotify playlist (Spotify developer
account + OAuth). Here it scrapes a bundled sample chart (chart_YYYY-MM-DD.html, fictional
songs) and writes a local playlist as both CSV and M3U.

**Topic:** Scraping + playlists

**Concepts:** scraping, CSV, M3U playlist files

## Notes

Account-free (replaced Billboard scraping + Spotify account/OAuth with a bundled fictional chart and local CSV/M3U playlists).

## Files

- `chart_1995-06-24.html`
- `chart_2000-08-12.html`
- `chart_2010-03-06.html`
- `main.py`
- `requirements.txt`

## Run

```bash
pip install -r requirements.txt
python main.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
