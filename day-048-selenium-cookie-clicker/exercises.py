"""Day 48 exercises: find elements by CSS selector to build an events dict, then fill in and
submit a form - all on the bundled events.html served locally. Needs Google Chrome."""
from pathlib import Path

from flask import Flask, send_from_directory
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from browser import make_driver
from local_server import LocalServer

app = Flask(__name__)


@app.get("/")
def page():
    return send_from_directory(Path(__file__).parent, "events.html")


def run() -> dict:
    with LocalServer(app) as server:
        driver = make_driver()
        try:
            driver.get(server.url)
            times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
            names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
            events = {i: {"time": t.get_attribute("datetime"), "name": n.text} for i, (t, n) in enumerate(zip(times, names))}
            print(events)
            driver.find_element(By.NAME, "fName").send_keys("Rishabh")
            driver.find_element(By.NAME, "lName").send_keys("Aryan")
            driver.find_element(By.NAME, "email").send_keys("rishabh@example.com", Keys.ENTER)
            print(driver.find_element(By.ID, "thanks").text)
            return events
        finally:
            driver.quit()


if __name__ == "__main__":
    run()
