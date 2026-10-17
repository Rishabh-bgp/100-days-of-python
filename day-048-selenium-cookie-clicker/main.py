"""Day 48 - Selenium Cookie Clicker bot: click the cookie non-stop and, every 5 seconds,
buy the most expensive upgrade you can afford. Stops after RUN_SECONDS and prints the rate.

Offline: drives the bundled cookie.html (a small cookie-clicker written for this repo)
served from 127.0.0.1, not the real orteil.dashnet.org game. Needs Google Chrome installed.
Selenium 4 style: By locators + Selenium Manager (no chromedriver path).
"""
import os
import time
from pathlib import Path

from flask import Flask, send_from_directory
from selenium.webdriver.common.by import By

from browser import make_driver
from local_server import LocalServer

HERE = Path(__file__).parent
RUN_SECONDS = int(os.environ.get("RUN_SECONDS", "30"))

app = Flask(__name__)


@app.get("/")
def game():
    return send_from_directory(HERE, "cookie.html")


def to_int(text: str) -> int:
    return int(text.replace(",", "").strip() or 0)


def run(seconds: int = RUN_SECONDS) -> str:
    with LocalServer(app) as server:
        driver = make_driver()
        try:
            driver.get(server.url)
            cookie = driver.find_element(By.ID, "cookie")
            next_check = time.time() + 5
            stop = time.time() + seconds
            while time.time() < stop:
                cookie.click()
                if time.time() >= next_check:
                    money = to_int(driver.find_element(By.ID, "money").text)
                    items = driver.find_elements(By.CSS_SELECTOR, "#store div")
                    affordable = [i for i in items if int(i.get_attribute("data-cost")) <= money]
                    if affordable:
                        max(affordable, key=lambda i: int(i.get_attribute("data-cost"))).click()
                    next_check = time.time() + 5
            rate = driver.find_element(By.ID, "cps").text
            print(f"Cookies {rate} after {seconds}s")
            return rate
        finally:
            driver.quit()


if __name__ == "__main__":
    run()
