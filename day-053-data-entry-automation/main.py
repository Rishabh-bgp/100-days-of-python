"""Day 53 - Data Entry Job Automation capstone: scrape rental listings with BeautifulSoup,
then use Selenium to type each one into a form, building a spreadsheet of results.

Account-free/offline: the course scrapes a Zillow clone and fills a Google Form (Google
account). This scrapes the bundled listings.html and fills a local Flask form
(form_site.py) that appends to responses.csv. Needs Google Chrome.
"""
import re
from pathlib import Path

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import form_site
from browser import make_driver
from local_server import LocalServer

HERE = Path(__file__).parent
BASE_URL = "https://rentals.example.com"


def scrape(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select(".StyledPropertyCard a.property-card-link") or soup.select("article a")
    prices = soup.select(".PropertyCardWrapper__StyledPriceLine") or soup.select("article span")
    rows = []
    for a, p in zip(links, prices):
        address = " ".join(a.get_text().replace("|", " ").split())
        price = re.split(r"[+/ ]", p.get_text().strip())[0]
        href = a["href"]
        rows.append({"address": address, "price": price, "link": href if href.startswith("http") else BASE_URL + href})
    return rows


def fill_forms(rows: list[dict]) -> int:
    with LocalServer(form_site.app) as server:
        driver = make_driver()
        wait = WebDriverWait(driver, 10)
        try:
            for row in rows:
                driver.get(server.url)
                for name in ("address", "price", "link"):
                    wait.until(EC.presence_of_element_located((By.NAME, name))).send_keys(row[name])
                driver.find_element(By.ID, "submit").click()
                wait.until(EC.presence_of_element_located((By.ID, "thanks")))
        finally:
            driver.quit()
    return len(rows)


def main() -> int:
    rows = scrape((HERE / "listings.html").read_text(encoding="utf-8"))
    print(f"Scraped {len(rows)} listings, e.g. {rows[0]}")
    n = fill_forms(rows)
    print(f"Submitted {n} form responses -> {form_site.RESPONSES.name}")
    return n


if __name__ == "__main__":
    main()
