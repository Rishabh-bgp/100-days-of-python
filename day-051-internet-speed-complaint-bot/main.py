"""Day 51 - Internet Speed Complaint Bot: a class that runs a speed test with Selenium and,
if the result is below what you pay for, posts a complaint.

Account-free: the course uses speedtest.net and Twitter/X (account; the X API is now paid).
This drives a local mock speed page and 'Chirp', a local mock social site with a fake login
(mock_site.py). Needs Google Chrome. HEADLESS=0 to watch.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import mock_site
from browser import make_driver
from local_server import LocalServer

PROMISED_DOWN, PROMISED_UP = 100, 20


class InternetSpeedBot:
    def __init__(self, base_url: str) -> None:
        self.base = base_url
        self.driver = make_driver()
        self.down = self.up = 0.0

    def get_internet_speed(self) -> tuple[float, float]:
        self.driver.get(f"{self.base}/speed")
        self.driver.find_element(By.ID, "go").click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, "status"), "Done"))
        self.down = float(self.driver.find_element(By.ID, "download-speed").text)
        self.up = float(self.driver.find_element(By.ID, "upload-speed").text)
        return self.down, self.up

    def post_complaint(self) -> str:
        self.driver.get(f"{self.base}/chirp")
        self.driver.find_element(By.ID, "email").send_keys("demo@example.com")
        self.driver.find_element(By.ID, "password").send_keys("demo-password")
        self.driver.find_element(By.ID, "login").click()
        text = (f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up "
                f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "compose"))).send_keys(text)
        self.driver.find_element(By.ID, "post").click()
        return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#timeline .post"))).text

    def quit(self) -> None:
        self.driver.quit()


def run() -> str | None:
    with LocalServer(mock_site.app) as server:
        bot = InternetSpeedBot(server.url)
        try:
            down, up = bot.get_internet_speed()
            print(f"Measured {down} down / {up} up")
            if down < PROMISED_DOWN or up < PROMISED_UP:
                posted = bot.post_complaint()
                print("Posted:", posted)
                return posted
            print("Speed is fine - no complaint.")
            return None
        finally:
            bot.quit()


if __name__ == "__main__":
    run()
