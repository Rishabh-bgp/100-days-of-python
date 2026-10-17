"""Day 92 - Portfolio project: custom web scraper. Crawl a paginated product listing,
extract title, price, star rating and stock, follow 'next' links, and export to CSV.

Offline: crawls the bundled sample_site/ (a fictional bookshop) by following local links,
so it never hits a real site. The same code works on a URL if you swap in a fetch function.

  python main.py                     # writes output/books.csv
"""
import csv
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup

HERE = Path(__file__).parent
START = (HERE / "sample_site" / "page-1.html").as_uri()
RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def fetch_local(url: str) -> str:
    return Path(url.removeprefix("file://")).read_text(encoding="utf-8")


def parse_page(html: str, base_url: str) -> tuple[list[dict], str | None]:
    soup = BeautifulSoup(html, "html.parser")
    books = []
    for pod in soup.select("article.product_pod") or soup.select("article"):
        link = pod.select_one("h3 a") or pod.find("a")
        price = pod.select_one(".price_color")
        rating_tag = pod.select_one("p.star-rating")
        rating = next((RATINGS[c] for c in (rating_tag.get("class", []) if rating_tag else []) if c in RATINGS), None)
        stock = pod.select_one(".availability")
        books.append({
            "title": link.get("title") or link.get_text(strip=True),
            "price_gbp": float(price.get_text(strip=True).lstrip("£")) if price else None,
            "rating": rating,
            "in_stock": bool(stock and "In stock" in stock.get_text()),
            "url": urljoin(base_url, link["href"]),
        })
    nxt = soup.select_one("li.next a")
    return books, urljoin(base_url, nxt["href"]) if nxt else None


def crawl(start: str = START, fetch=fetch_local, max_pages: int = 50) -> list[dict]:
    rows, url, pages = [], start, 0
    while url and pages < max_pages:
        books, url = parse_page(fetch(url), url)
        rows += books
        pages += 1
    print(f"Crawled {pages} pages, {len(rows)} products")
    return rows


def main() -> Path:
    rows = crawl()
    out = HERE / "output" / "books.csv"
    out.parent.mkdir(exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    best = max((r for r in rows if r["in_stock"]), key=lambda r: (r["rating"] or 0, -(r["price_gbp"] or 0)))
    print(f"Saved {out.relative_to(HERE)}. Best in-stock pick: {best['title']} ({best['rating']}★, £{best['price_gbp']})")
    return out


if __name__ == "__main__":
    main()
