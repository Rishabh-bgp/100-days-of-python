"""Selenium 4 Chrome driver factory. Selenium Manager finds/downloads the right driver
automatically - no manual chromedriver path. Set HEADLESS=0 to watch the bot work."""
import os

from selenium import webdriver


def make_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    if os.environ.get("HEADLESS", "1") != "0":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("detach", os.environ.get("HEADLESS") == "0")
    return webdriver.Chrome(options=options)
