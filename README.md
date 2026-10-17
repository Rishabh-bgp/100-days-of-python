# 100 Days of Python: my project solutions

![Python](https://img.shields.io/badge/python-3.12%2B-blue) ![License: MIT](https://img.shields.io/badge/license-MIT-green) ![No API keys](https://img.shields.io/badge/API%20keys-none%20needed-brightgreen)

My own solutions to the daily projects and exercises from the **100 Days of Code: The Complete Python Pro Bootcamp** curriculum, one folder per day.

> **Not affiliated with the course.** These are independent solutions written from the publicly listed project topics. No course code, starter files, text, images or other materials are included. If you want the lessons, take the course: [100 Days of Code by Dr. Angela Yu on Udemy](https://www.udemy.com/course/100-days-of-code/).

**Progress:** 25 done · 0 partial · 75 pending

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

| Day | Project | Topic | Status | Modernised / replaced |
|---:|---|---|---|---|
| 1 | [Band Name Generator](day-001-band-name-generator/) | Basics | ✅ done |  |
| 2 | [Tip Calculator](day-002-tip-calculator/) | Basics | ✅ done |  |
| 3 | [Treasure Island](day-003-treasure-island/) | Control flow | ✅ done |  |
| 4 | [Rock Paper Scissors](day-004-rock-paper-scissors/) | Randomisation & lists | ✅ done |  |
| 5 | [Password Generator](day-005-password-generator/) | Loops | ✅ done | Uses the `secrets` module (cryptographically secure) instead of `random` for passwords. |
| 6 | [Reeborg's World Maze](day-006-reeborgs-world-maze/) | Functions & while loops | ✅ done | Offline: a small text-grid robot simulator (robot.py) replaces the Reeborg's World website. |
| 7 | [Hangman](day-007-hangman/) | Flow & logic | ✅ done |  |
| 8 | [Caesar Cipher](day-008-caesar-cipher/) | Function parameters | ✅ done |  |
| 9 | [Secret Auction](day-009-secret-auction/) | Dictionaries | ✅ done |  |
| 10 | [Calculator](day-010-calculator/) | Functions with outputs | ✅ done | Uses the `operator` module and handles divide-by-zero. |
| 11 | [Blackjack](day-011-blackjack/) | Capstone 1 | ✅ done |  |
| 12 | [Number Guessing Game](day-012-number-guessing-game/) | Scope | ✅ done |  |
| 13 | [Debugging exercises](day-013-debugging/) | Debugging | ✅ done |  |
| 14 | [Higher Lower Game](day-014-higher-lower-game/) | Practice project | ✅ done | Original fictional sample accounts replace the course data. |
| 15 | [Coffee Machine](day-015-coffee-machine/) | Local dev environment | ✅ done |  |
| 16 | [OOP Coffee Machine](day-016-oop-coffee-machine/) | OOP | ✅ done | A stdlib table class replaces the third-party `prettytable` demo. |
| 17 | [Quiz Game](day-017-quiz-game/) | Creating classes | ✅ done | API-free (replaced Open Trivia DB with a bundled questions.json). |
| 18 | [Hirst Spot Painting](day-018-hirst-painting/) | Turtle & GUIs | ✅ done | Hand-picked palette replaces `colorgram` colour extraction. GUI. |
| 19 | [Etch-A-Sketch & Turtle Race](day-019-etch-a-sketch-and-turtle-race/) | Instances & events | ✅ done | GUI. |
| 20 | [Snake Game (part 1)](day-020-snake-game-part-1/) | Animation & coordinates | ✅ done | GUI. |
| 21 | [Snake Game (part 2)](day-021-snake-game-part-2/) | Inheritance & slicing | ✅ done | Includes the Day 24 high-score file upgrade. GUI. |
| 22 | [Pong](day-022-pong/) | Arcade game | ✅ done | GUI. |
| 23 | [Turtle Crossing](day-023-turtle-crossing/) | Capstone 2 | ✅ done | GUI. |
| 24 | [Mail Merge](day-024-mail-merge/) | Files & paths | ✅ done | Uses `pathlib`. |
| 25 | [U.S. States Game](day-025-us-states-game/) | CSV & pandas | ✅ done | Draws positions from a CSV (no course image); squirrel census uses a synthetic dataset. Map game is GUI. |
| 26 | NATO Alphabet | Comprehensions | ⏳ pending |  |
| 27 | Mile to Km Converter | tkinter, *args, **kwargs | ⏳ pending | GUI. |
| 28 | Pomodoro Timer | tkinter events | ⏳ pending | Tomato drawn on the canvas instead of an image asset. GUI. |
| 29 | Password Manager | tkinter layout | ⏳ pending | tkinter clipboard replaces `pyperclip`. GUI. |
| 30 | Password Manager (JSON) | Errors & JSON | ⏳ pending | GUI. |
| 31 | Flash Card App | Capstone 3 | ⏳ pending | Original French word list; card faces drawn on canvas. GUI. |
| 32 | Automated Birthday Wisher | Email & datetime | ⏳ pending | Account-free (replaced Gmail SMTP login with a local outbox/ folder or a local aiosmtpd debug server). |
| 33 | ISS Overhead Notifier | APIs (offline) | ⏳ pending | API-free (replaced Open Notify + sunrise-sunset.org with offline orbit and NOAA solar formulas; Kanye API with bundled quotes; email with local outbox). |
| 34 | Quizzler | GUI + type hints | ⏳ pending | API-free (replaced Open Trivia DB with bundled questions.json). GUI. |
| 35 | Rain Alert | API keys & SMS (offline) | ⏳ pending | API-free (replaced OpenWeather with a bundled sample forecast; Twilio SMS with local outbox). |
| 36 | Stock News Alert | Capstone: APIs (offline) | ⏳ pending | API-free (replaced Alpha Vantage, NewsAPI and Twilio with bundled sample prices/news and local outbox). |
| 37 | Habit Tracker | HTTP verbs (offline) | ⏳ pending | API-free (replaced Pixela account + token with local SQLite and a matplotlib graph). |
| 38 | Workout Tracker | NLP & sheets (offline) | ⏳ pending | API-free (replaced Nutritionix with a local MET table parser; Google Sheets/Sheety with SQLite + CSV). |
| 39 | Flight Deal Finder | Classes working together | ⏳ pending | API-free (replaced Sheety, Tequila/Kiwi (shut down) and Twilio with local CSVs, synthetic flight data and outbox). |
| 40 | Flight Club | Capstone: users | ⏳ pending | Account-free (replaced Google Form/Sheet with local SQLite; Gmail with local outbox). |
| 41 | Personal Site (HTML) | HTML intro | ⏳ pending |  |
| 42 | Intermediate HTML | HTML tables & forms | ⏳ pending |  |
| 43 | Intro to CSS | CSS basics | ⏳ pending |  |
| 44 | Intermediate CSS | Box model & layout | ⏳ pending |  |
| 45 | Top Movies Scraper | BeautifulSoup | ⏳ pending | Offline (scrapes bundled sample HTML; selectors have fallbacks). |
| 46 | Musical Time Machine | Scraping + playlists | ⏳ pending | Account-free (replaced Billboard scraping + Spotify account/OAuth with a bundled fictional chart and local CSV/M3U playlists). |
| 47 | Price Tracker | Scraping + alerts | ⏳ pending | Account-free (replaced live Amazon scraping + Gmail with a bundled product page and local outbox). |
| 48 | Cookie Clicker Bot | Selenium | ⏳ pending | Offline (drives a bundled local cookie-clicker page). Selenium (local mock). |
| 49 | Job Application Bot | Selenium automation | ⏳ pending | Account-free (replaced LinkedIn with 'MockedIn', a local Flask mock with a fake login). Selenium (local mock). |
| 50 | Auto-Swipe Bot | Selenium popups | ⏳ pending | Account-free (replaced Tinder with 'Swipr', a local Flask mock). Selenium (local mock). |
| 51 | Internet Speed Complaint Bot | Selenium + classes | ⏳ pending | Account-free (replaced speedtest.net + Twitter/X with a local mock speed page and 'Chirp' mock social site). Selenium (local mock). |
| 52 | Follower Bot | Selenium scrolling | ⏳ pending | Account-free (replaced Instagram with 'Pictagram', a local Flask mock). Selenium (local mock). |
| 53 | Data Entry Automation | Capstone: scrape + automate | ⏳ pending | Account-free (replaced Zillow clone + Google Forms with bundled listings HTML and a local Flask form that saves to CSV). Selenium (local mock). |
| 54 | Intro to Flask | Flask & decorators | ⏳ pending |  |
| 55 | Higher Lower (URLs) | Flask routing | ⏳ pending |  |
| 56 | Name Card Website | Templates & static files | ⏳ pending |  |
| 57 | Blog Templating | Jinja | ⏳ pending | API-free (replaced agify/genderize/npoint APIs with bundled JSON and a local guess function). |
| 58 | TinDog (Bootstrap) | Bootstrap | ⏳ pending | Bootstrap 5 from CDN-free local markup (no external account). |
| 59 | Blog Capstone pt 2 | Styling a blog | ⏳ pending |  |
| 60 | HTML Forms + Flask | POST requests | ⏳ pending | Account-free (contact form emails go to a local outbox). |
| 61 | Flask-WTF Login | Flask-WTF | ⏳ pending | Bootstrap-Flask replaces the dead Flask-Bootstrap. |
| 62 | Coffee & Wi-Fi | Flask-WTF + CSV | ⏳ pending | Bootstrap-Flask replaces Flask-Bootstrap. |
| 63 | Virtual Bookshelf | SQLite + SQLAlchemy | ⏳ pending | SQLAlchemy 2.0-style queries. |
| 64 | Top 10 Movies | SQLAlchemy + forms | ⏳ pending | API-free (replaced TMDB search with a bundled movie catalogue). |
| 65 | Web Design Landing Page | Design principles | ⏳ pending |  |
| 66 | Cafe REST API | Build a REST API | ⏳ pending | The API key is a local demo value checked by your own app. |
| 67 | Blog Capstone pt 3 | RESTful blog | ⏳ pending | A plain textarea replaces Flask-CKEditor. |
| 68 | Flask Authentication | Auth | ⏳ pending | Users register in the app's own local SQLite (no external account). |
| 69 | Blog Capstone pt 4 | Users & comments | ⏳ pending | Local SQLite users; Gravatar replaced by local initials avatars. |
| 70 | Deploying (locally) | Git & deployment | ⏳ pending | Account-free (replaced Heroku/Render hosting with local gunicorn + optional Docker). |
| 71 | College Majors Analysis | pandas exploration | ⏳ pending | Offline synthetic dataset generated by script. |
| 72 | Programming Languages Popularity | matplotlib | ⏳ pending | Offline synthetic dataset. |
| 73 | LEGO Dataset Analysis | Aggregation & merging | ⏳ pending | Offline synthetic dataset. |
| 74 | Trends & Resampling | Time series | ⏳ pending | Offline synthetic dataset. |
| 75 | App Store Analysis | Plotly | ⏳ pending | Offline synthetic dataset; charts saved as HTML. |
| 76 | NumPy N-dimensional arrays | NumPy | ⏳ pending |  |
| 77 | Movie Budgets & Revenue | Seaborn & regression | ⏳ pending | Offline synthetic dataset. |
| 78 | Nobel Prize Analysis | Data analysis | ⏳ pending | Offline synthetic dataset. |
| 79 | Handwashing Discovery | Statistics | ⏳ pending | Offline synthetic dataset modelled on the story. |
| 80 | House Price Prediction | Multivariable regression | ⏳ pending | Offline synthetic dataset. |
| 81 | US Police Data Analysis | Capstone: data | ⏳ pending | Offline synthetic dataset. |
| 82 | Text to Morse Code | Portfolio | ⏳ pending |  |
| 83 | Tic Tac Toe | Portfolio | ⏳ pending |  |
| 84 | Image Watermarker | Portfolio | ⏳ pending | GUI. Core watermark function also works from the CLI. |
| 85 | Typing Speed Test | Portfolio | ⏳ pending | GUI. |
| 86 | Breakout | Portfolio | ⏳ pending | GUI. |
| 87 | Cafe & Wi-Fi Website | Portfolio | ⏳ pending |  |
| 88 | To-Do List Website | Portfolio | ⏳ pending |  |
| 89 | Disappearing Text Writing App | Portfolio | ⏳ pending | GUI. |
| 90 | PDF to Audiobook | Portfolio | ⏳ pending | Offline (replaced cloud TTS APIs with a local engine: espeak/pyttsx3 if present, else a WAV tone fallback). |
| 91 | Image Colour Palette | Portfolio | ⏳ pending |  |
| 92 | Custom Web Scraper | Portfolio | ⏳ pending | Offline (bundled sample site). |
| 93 | Dino Game Bot | Portfolio | ⏳ pending | Offline (local dino-runner page). Selenium (local mock). |
| 94 | Space Invaders | Portfolio | ⏳ pending | GUI. |
| 95 | Custom API-based Website | Portfolio | ⏳ pending | API-free (the site serves and consumes its own local JSON API). |
| 96 | Online Shop | Portfolio | ⏳ pending | Account-free (replaced Stripe with a mock local checkout). |
| 97 | Custom Automation | Portfolio | ⏳ pending |  |
| 98 | Custom Data Analysis | Portfolio | ⏳ pending | Offline synthetic dataset. |
| 99 | Space Race Analysis | Portfolio | ⏳ pending | Offline synthetic dataset. |
| 100 | Predict Earnings (Regression) | Portfolio | ⏳ pending | Offline synthetic dataset. |

## Verification

`python tools/verify.py` byte-compiles every file, runs `ruff` for errors, and smoke-tests the CLI projects with piped input, the Flask apps with their test client, and the data scripts headlessly. The results of the last run are in [VERIFICATION.md](VERIFICATION.md).

## Contributing

Improvements and alternative solutions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). This repo takes part in Hacktoberfest.

## Credits & licence

- The project ideas follow the public curriculum of *100 Days of Code: The Complete Python Pro Bootcamp* by Dr. Angela Yu (London App Brewery). All code, data and text here are original.
- Sample data (questions, words, charts, prices, listings and so on) is original or synthetic and made up for practice.
- Licensed under the [MIT License](LICENSE) © 2026 Rishabh Aryan.
