"""Day 47 - Price Tracker: scrape a product price and send an alert if it's below your target.

Account-free/offline: the course scrapes Amazon (which blocks bots and needs headers) and
emails via Gmail SMTP. Here it parses the bundled product_page.html (or any saved page you
pass) and the alert goes to a local outbox / local debug SMTP server.
"""
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

from outbox import send_email

HERE = Path(__file__).parent
TARGET_PRICE = 8000.0
PRICE_SELECTORS = ["span.a-price span.a-offscreen", "span.a-price-whole", "[itemprop=price]", ".price"]


def parse_price(html: str) -> tuple[str, float]:
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.select_one("#productTitle") or soup.find("title")
    title = " ".join(title_tag.get_text().split()) if title_tag else "Unknown product"
    for sel in PRICE_SELECTORS:
        tag = soup.select_one(sel)
        if tag:
            digits = re.sub(r"[^\d.]", "", tag.get("content") or tag.get_text())
            if digits:
                return title, float(digits)
    raise ValueError("Price not found - the page layout may have changed.")


def main(page: Path = HERE / "product_page.html", target: float = TARGET_PRICE) -> bool:
    title, price = parse_price(page.read_text(encoding="utf-8"))
    print(f"{title}: ₹{price:,.2f} (target ₹{target:,.2f})")
    if price < target:
        send_email("me@example.com", "Price drop alert!", f"{title} is now ₹{price:,.2f}.\nBuy it here: {page.name}")
        return True
    return False


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "product_page.html")
