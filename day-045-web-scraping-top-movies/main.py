"""Day 45 - Web scraping with BeautifulSoup: extract the movie list and save it in order.

Offline: scrapes the bundled sample_pages/top_movies.html (written for this repo) instead
of a live website, so it always works. Selectors have fallbacks in case the markup changes;
point SOURCE at another file or pass a URL-downloaded HTML file to try your own.
"""
import sys
from pathlib import Path

from bs4 import BeautifulSoup

HERE = Path(__file__).parent
SOURCE = HERE / "sample_pages" / "top_movies.html"
SELECTORS = ["article.movie-card h3.title", "h3.title", "h3"]


def extract_titles(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    for selector in SELECTORS:
        tags = soup.select(selector)
        if tags:
            return [t.get_text(strip=True) for t in tags]
    return []


def main(src: Path = SOURCE) -> list[str]:
    titles = extract_titles(src.read_text(encoding="utf-8"))[::-1]
    out = HERE / "movies.txt"
    out.write_text("\n".join(titles) + "\n", encoding="utf-8")
    print(f"Saved {len(titles)} titles to {out.name}. First: {titles[0]!r}")
    return titles


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else SOURCE)
