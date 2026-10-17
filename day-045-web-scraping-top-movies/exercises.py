"""Day 45 exercises: find_all/select, attributes, and the 'highest-voted story' challenge
on a bundled sample news board (sample_pages/news.html)."""
from pathlib import Path

from bs4 import BeautifulSoup

PAGE = Path(__file__).parent / "sample_pages" / "news.html"


def stories(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("span.titleline > a") or soup.select("td.title a")
    scores = [int(s.get_text().split()[0]) for s in soup.select("span.score")]
    return [{"title": a.get_text(), "link": a.get("href"), "points": p} for a, p in zip(links, scores)]


def top_story(html: str) -> dict:
    return max(stories(html), key=lambda s: s["points"])


if __name__ == "__main__":
    html = PAGE.read_text(encoding="utf-8")
    for s in stories(html):
        print(f"{s['points']:>4}  {s['title']}")
    print("Top:", top_story(html))
