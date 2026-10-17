"""Day 52 - Follower Bot: open a similar account's followers list, scroll the modal, and
click Follow on everyone (cancelling the 'Unfollow?' dialog for people already followed).

Account-free: the course automates Instagram (real account, against its terms). This drives
'Pictagram', a local mock (mock_site.py) with a fake login. Needs Google Chrome.
"""
import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import mock_site
from browser import make_driver
from local_server import LocalServer


class FollowerBot:
    def __init__(self, base: str) -> None:
        self.base = base
        self.driver = make_driver()

    def login(self) -> None:
        self.driver.get(self.base)
        self.driver.find_element(By.ID, "email").send_keys("demo@example.com")
        self.driver.find_element(By.ID, "password").send_keys("demo-password")
        self.driver.find_element(By.ID, "login").click()

    def find_followers(self, scrolls: int = 5) -> None:
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "followers-link"))).click()
        modal = self.driver.find_element(By.ID, "modal-list")
        for _ in range(scrolls):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(0.2)

    def follow(self) -> int:
        clicked = 0
        for button in self.driver.find_elements(By.CSS_SELECTOR, ".follow-btn"):
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", button)
            try:
                button.click()
                if self.driver.find_elements(By.ID, "confirm"):
                    self.driver.find_element(By.ID, "cancel").click()
                    continue
                clicked += 1
            except ElementClickInterceptedException:
                self.driver.find_element(By.ID, "cancel").click()
        return clicked


def run() -> int:
    with LocalServer(mock_site.app) as server:
        bot = FollowerBot(server.url)
        try:
            bot.login()
            bot.find_followers()
            n = bot.follow()
        finally:
            bot.driver.quit()
    print(f"Followed {n} new accounts; now following {len(mock_site.FOLLOWING)} in total.")
    return n


if __name__ == "__main__":
    run()
