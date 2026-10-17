# 100 Days of Python: my project solutions

![Python](https://img.shields.io/badge/python-3.12%2B-blue) ![License: MIT](https://img.shields.io/badge/license-MIT-green) ![No API keys](https://img.shields.io/badge/API%20keys-none%20needed-brightgreen)

My own solutions to the daily projects and exercises from the **100 Days of Code: The Complete Python Pro Bootcamp** curriculum, one folder per day.

> **Not affiliated with the course.** These are independent solutions written from the publicly listed project topics. No course code, starter files, text, images or other materials are included. If you want the lessons, take the course: [100 Days of Code by Dr. Angela Yu on Udemy](https://www.udemy.com/course/100-days-of-code/).

**Progress:** {{DONE}} done · {{PARTIAL}} partial · {{PENDING}} pending

## What's different from the original course approach

The course is several years old and parts of it no longer run as filmed. This repo is updated for current tools, and **every project runs offline, with no API keys and no accounts**:

- **Python 3.12+**, type hints and `pathlib` throughout. Tested with Python 3.13.
- **No external APIs.** Web APIs (Open Trivia DB, OpenWeather, Twilio, Alpha Vantage, NewsAPI, Pixela, Nutritionix, Sheety, Tequila/Kiwi, TMDB and so on) are replaced with bundled sample data (JSON/CSV), synthetic data or offline formulas. The learning goal of each day stays the same.
- **No accounts anywhere.** Email goes to a local `outbox/` folder or a local `aiosmtpd` debug server instead of Gmail. Google Sheets becomes SQLite/CSV. Spotify becomes local CSV/M3U playlists. Hosting becomes local gunicorn plus an optional Dockerfile.
- **Bots run against local mock sites.** The LinkedIn, Tinder, Twitter/X, Instagram, Zillow/Google Forms and cookie-clicker bots drive small bundled Flask/HTML mock sites with fake logins on `127.0.0.1`.
- **Selenium 4:** `By` locators and Selenium Manager, so there's no `find_element_by_*` and no manual chromedriver path.
- **pandas 2+/3:** no `DataFrame.append` (`concat` instead). **Flask 3**, **Flask-SQLAlchemy 3.1** (`db.session.get`, SQLAlchemy 2.0-style `select`), **WTForms 3**, and **Bootstrap-Flask** instead of the dead Flask-Bootstrap.
- **Scraping:** selectors have fallbacks and run against bundled sample HTML, so they don't break when a live site changes.
- Each day's `requirements.txt` pins the versions it was tested with.

## Running a project

```bash
git clone https://github.com/Rishabh-bgp/100-days-of-python.git
cd 100-days-of-python/day-003-treasure-island
python main.py
```

Days with third-party libraries have their own `requirements.txt`. A virtual environment is recommended:

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r day-063-virtual-bookshelf/requirements.txt
```

GUI days (turtle/tkinter) need a desktop; on Linux install `python3-tk`. Selenium days need Google Chrome.

## All 100 days
