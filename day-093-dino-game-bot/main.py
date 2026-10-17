"""Day 93 - Portfolio project: bot that plays a dinosaur runner game by itself.
Selenium reads the obstacle positions from the page and presses Space just in time.

Offline: the course targets Chrome's built-in dino game / an online copy. This plays the
bundled dino.html (a small runner written for this repo) served on 127.0.0.1.
Needs Google Chrome. Set HEADLESS=0 to watch; RUN_SECONDS to change how long it plays.
"""
import os
import time
from pathlib import Path

from flask import Flask, send_from_directory
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from browser import make_driver
from local_server import LocalServer

RUN_SECONDS = int(os.environ.get("RUN_SECONDS", "20"))
app = Flask(__name__)

NEAREST_JS = """
const xs=[...document.querySelectorAll('.cactus')].map(c=>+c.dataset.x).filter(x=>x>40);
return xs.length?Math.min(...xs):9999;"""


@app.get("/")
def game():
    return send_from_directory(Path(__file__).parent, "dino.html")


def play(seconds: int = RUN_SECONDS) -> int:
    with LocalServer(app) as server:
        driver = make_driver()
        try:
            driver.get(server.url)
            body = driver.find_element(By.TAG_NAME, "body")
            body.send_keys(Keys.SPACE)
            end = time.time() + seconds
            while time.time() < end and driver.find_element(By.ID, "status").text != "GAME OVER":
                speed = 6 + int(driver.find_element(By.ID, "score").text) / 600
                if driver.execute_script(NEAREST_JS) < 80 + speed * 8:
                    body.send_keys(Keys.SPACE)
                time.sleep(0.01)
            score = int(driver.find_element(By.ID, "score").text)
            status = driver.find_element(By.ID, "status").text
            print(f"{status}: score {score} after {seconds}s")
            return score
        finally:
            driver.quit()


if __name__ == "__main__":
    play()
