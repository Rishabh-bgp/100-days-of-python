"""Day 50 - Auto-swiping bot (Selenium): log in, dismiss the cookie and location popups,
press Like repeatedly, close "It's a match!" overlays, and stop at the daily like limit.

Account-free: the course automates Tinder (real account). This drives 'Swipr', a local mock
(mock_site.py) with a fake login. Needs Google Chrome. HEADLESS=0 to watch.
"""
import time

from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import mock_site
from browser import make_driver
from local_server import LocalServer


def run(max_swipes: int = 100) -> int:
    with LocalServer(mock_site.app) as server:
        driver = make_driver()
        try:
            driver.get(server.url)
            driver.find_element(By.ID, "email").send_keys("demo@example.com")
            driver.find_element(By.ID, "password").send_keys("demo-password")
            driver.find_element(By.ID, "login").click()
            # popups stack: the newest (location) is on top, so close it first
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "allow-location"))).click()
            driver.find_element(By.ID, "accept-cookies").click()
            for _ in range(max_swipes):
                time.sleep(0.3)
                if driver.find_elements(By.ID, "out-of-likes"):
                    print("Out of likes for today.")
                    break
                try:
                    driver.find_element(By.ID, "like").click()
                except ElementClickInterceptedException:
                    try:
                        driver.find_element(By.ID, "back-to-swiping").click()
                        print("Match popup dismissed.")
                    except NoSuchElementException:
                        time.sleep(0.5)
        finally:
            driver.quit()
    print(f"Liked {len(mock_site.LIKES)} profiles.")
    return len(mock_site.LIKES)


if __name__ == "__main__":
    run()
