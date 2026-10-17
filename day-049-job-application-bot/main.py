"""Day 49 - Automated job application bot (Selenium): log in, open each job, save it, and
submit the "Easy Apply" ones that only need a phone number; skip multi-step applications.

Account-free: the course automates LinkedIn (real account, against its terms). This bot
drives 'MockedIn', a local Flask mock (mock_site.py) with a fake login, started on
127.0.0.1 automatically. Needs Google Chrome. HEADLESS=0 to watch.
"""
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import mock_site
from browser import make_driver
from local_server import LocalServer

EMAIL = os.environ.get("MOCK_EMAIL", "demo@example.com")
PASSWORD = os.environ.get("MOCK_PASSWORD", "demo-password")  # mock-site demo password, not a secret
PHONE = os.environ.get("MOCK_PHONE", "9999999999")


def run() -> dict:
    result = {"applied": [], "skipped": []}
    with LocalServer(mock_site.app) as server:
        driver = make_driver()
        driver.implicitly_wait(2)
        try:
            driver.get(server.url)
            driver.find_element(By.ID, "username").send_keys(EMAIL)
            driver.find_element(By.ID, "password").send_keys(PASSWORD)
            driver.find_element(By.ID, "sign-in").click()
            links = [a.get_attribute("href") for a in driver.find_elements(By.CSS_SELECTOR, "a.job-link")]
            for link in links:
                driver.get(link)
                title = driver.find_element(By.ID, "job-title").text
                save_btn = driver.find_element(By.CSS_SELECTOR, ".save-btn")
                save_btn.click()
                WebDriverWait(driver, 5).until(EC.staleness_of(save_btn))  # wait for the page reload
                try:
                    phone = driver.find_element(By.ID, "phone")
                except NoSuchElementException:
                    print(f"Skipped (complex application): {title}")
                    result["skipped"].append(title)
                    continue
                phone.clear()
                phone.send_keys(PHONE)
                driver.find_element(By.ID, "submit-application").click()
                driver.find_element(By.ID, "applied")
                print(f"Applied: {title}")
                result["applied"].append(title)
        finally:
            driver.quit()
    print(f"Done: {len(result['applied'])} applied, {len(result['skipped'])} skipped. "
          f"Server recorded {len(mock_site.APPLICATIONS)} applications.")
    return result


if __name__ == "__main__":
    run()
