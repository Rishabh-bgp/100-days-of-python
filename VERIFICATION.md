# Verification report

Python 3.13.5; days 1-75.

## py_compile

140/140 files compile.

## ruff (pyflakes rules F + syntax errors E9)

```
[1;32mAll checks passed![0m
```

## CLI / script smoke tests (piped input)

| Day | Command | Result | Last output line |
|---:|---|---|---|
| 1 | `main.py` | pass | > Your band name could be: Bhopal Tiger |
| 1 | `exercises.py` | pass | swap(3, 5) -> (5, 3) |
| 2 | `main.py` | pass | What was the total bill? $What percentage tip would you like to give? 10, 12, or 15? How many people to split the bill? Each person should p |
| 2 | `exercises.py` | pass | You have 3380 weeks left. |
| 3 | `main.py` | pass | You reach a crossroad. Go "left" or "right"? You reach a lake. "wait" for a boat or "swim" across? You reach an island house with a "red", " |
| 3 | `exercises.py` | pass | Your score is 53. |
| 4 | `main.py` | pass | It's a draw. |
| 4 | `exercises.py` | pass | ⬜️ X ⬜️ |
| 5 | `main.py` | pass | > Your password is: wl+v4d4!YDww3 |
| 5 | `exercises.py` | pass | 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz |
| 6 | `main.py` | pass | Reeborg reached the goal in 26 moves! |
| 6 | `exercises.py` | pass | Hurdles finished in 34 moves |
| 7 | `main.py` | pass | You lose! The word was 'jigsaw'. |
| 8 | `main.py` | pass | > Goodbye |
| 8 | `exercises.py` | pass | Primes under 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] |
| 9 | `main.py` | pass | The winner is Ben with a bid of $150.00 |
| 9 | `exercises.py` | pass | [{'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']}, {'country': 'India', 'visits': 3, 'cities': ['Delhi', 'Bhopal'] |
| 10 | `main.py` | pass | Type 'y' to continue with 4.0, 'n' to start again, or 'q' to quit: |
| 10 | `exercises.py` | pass | Feb 2024 has 29 days |
| 11 | `main.py` | pass | Do you want to play a game of Blackjack? Type 'y' or 'n': |
| 12 | `main.py` | pass | You've run out of guesses. The answer was 94. |
| 12 | `exercises.py` | pass | 73 It's a prime number. |
| 13 | `exercises.py` | pass | even ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'] |
| 14 | `main.py` | pass | Who has more followers? Type 'A' or 'B': Sorry, that's wrong. Final score: 0 |
| 15 | `main.py` | pass | What would you like? (espresso/latte/cappuccino): Turning off. Goodbye! |
| 16 | `main.py` | pass | What would you like? (latte/espresso/cappuccino): |
| 16 | `exercises.py` | pass | +--------------+----------+ |
| 17 | `main.py` | pass | You've completed the quiz. Final score: 5/12 |
| 24 | `main.py` | pass | Wrote 7 letters to Output/ReadyToSend/ |
| 24 | `exercises.py` | pass | absolute path example: /tmp/tmpq18it3xh/data.txt |
| 25 | `exercises.py` | pass | 2     Black    146 |
| 25 | `-c "import main; d=main.load_states(); print(main.check_g...` | pass | 49 |
| 26 | `main.py` | pass | Enter a word: ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar', 'Whiskey', 'Oscar', 'Romeo', 'Lima', 'Delta'] |
| 26 | `exercises.py` | pass | {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0} |
| 27 | `exercises.py` | pass | Tata None |
| 28 | `-c "import main; print(main.session_for(1), main.session_...` | pass | (25, 'Work', '#9bdeac') (20, 'Break', '#e7305b') 2:05 |
| 29 | `-c "import main, tempfile, pathlib; p=pathlib.Path(tempfi...` | pass | site / a@b.c / &J5FUo90d(eZkp(w |
| 30 | `exercises.py` | pass | Caught: Human height should not be over 3 metres. |
| 30 | `-c "import vault, tempfile, pathlib; p=pathlib.Path(tempf...` | pass | {'email': 'me@x.com', 'password': 'pw1'} None |
| 31 | `-c "import deck; d=deck.Deck(); c=d.next_card(); d.mark_k...` | pass | {'French': 'le travail', 'English': 'the work'} 39 |
| 32 | `main.py 2026-10-18` | pass | 1 birthday email(s) written to outbox/ for 2026-10-18. |
| 32 | `monday_motivation.py --force` | pass | The best way to learn to code is to write code. |
| 33 | `main.py 6` | pass | No overhead night-time pass in the window. |
| 33 | `-c "from astro import *; from datetime import datetime, t...` | pass | (datetime.datetime(2026, 6, 21, 0, 4, 40, 173346, tzinfo=datetime.timezone.utc), datetime.datetime(2026, 6, 21, 13, 38, 42, 415070, tzinfo=d |
| 34 | `-c "from quiz_brain import *; q=QuizBrain(load_questions(...` | pass | Q.1: Python lists are immutable. False |
| 35 | `main.py` | pass | It's going to rain today. Remember to bring an ☔️ |
| 35 | `main.py sample_forecast_dry.json` | pass | No rain expected in the next 12 hours. |
| 36 | `main.py` | pass | Brief: Comments focused on autonomy and software updates. |
| 37 | `main.py demo` | pass | 2026-10-17 2.3 |
| 37 | `main.py add 2026-01-01 3` | pass | 2026-10-17 2.3 |
| 37 | `main.py update 2026-01-01 4.5` | pass | 2026-10-17 2.3 |
| 37 | `main.py delete 2026-01-01` | pass | 2026-10-17 2.3 |
| 38 | `main.py` | pass | Saved to workouts.db and workouts.csv |
| 39 | `main.py` | pass | 2 deal(s) found. |
| 40 | `main.py signup` | pass | > You're in the club! |
| 40 | `main.py deals` | pass | Sent 5 email(s) to 1 member(s). |
| 45 | `main.py` | pass | Saved 30 titles to movies.txt. First: '1) The Shawshank Redemption' |
| 45 | `exercises.py` | pass | Top: {'title': 'Why SQLite is everywhere', 'link': 'https://example.com/sqlite', 'points': 541} |
| 46 | `main.py` | pass | Which year do you want to travel to? Type the date in YYYY-MM-DD format ['1995-06-24', '2000-08-12', '2010-03-06']: Wrote 100 songs to 2000- |
| 47 | `main.py` | pass | Buy it here: product_page.html |
| 54 | `exercises.py` | pass | slow_function run speed: 0.3632s |
| 63 | `sqlite_basics.py` | pass | ['Sample Book: 9.5', 'Another Book: 7.5'] |
| 71 | `analysis.py` | pass | STEM                     70420.0                  123350.0 |
| 72 | `analysis.py` | pass | saved output/languages.png |
| 73 | `analysis.py` | pass | saved charts to output/ |
| 74 | `analysis.py` | pass | saved charts to output/ |
| 75 | `analysis.py` | pass | saved interactive charts (HTML) to output/ |

## Flask test-client checks

| Day | Command | Result | Last output line |
|---:|---|---|---|
| 54 | `../tools/flask_smoke.py / /bye` | pass | GET /bye -> 200 |
| 55 | `../tools/flask_smoke.py / /3 /greet/Rishabh/25` | pass | GET /greet/Rishabh/25 -> 200 |
| 56 | `../tools/flask_smoke.py /` | pass | GET / -> 200 |
| 57 | `../tools/flask_smoke.py / /post/1 /guess/rishabh` | pass | GET /guess/rishabh -> 200 |
| 58 | `../tools/flask_smoke.py /` | pass | GET / -> 200 (local bootstrap css 200) |
| 59 | `../tools/flask_smoke.py / /post/2 /about /contact` | pass | GET /contact -> 200 (local bootstrap css 200) |
| 60 | `../tools/flask_smoke.py / /contact` | pass | GET /contact -> 200 |
| 61 | `../tools/flask_smoke.py / /login` | pass | GET /login -> 200 (local bootstrap css 200) |
| 62 | `../tools/flask_smoke.py / /add /cafes` | pass | GET /cafes -> 200 (local bootstrap css 200) |
| 63 | `../tools/flask_smoke.py / /add` | pass | GET /add -> 200 |
| 64 | `../tools/flask_smoke.py / /add /edit?id=1` | pass | GET /edit?id=1 -> 200 (local bootstrap css 200) |
| 66 | `../tools/flask_smoke.py / /random /all /search?loc=MG` | pass | GET /search?loc=MG -> 200 |
| 67 | `../tools/flask_smoke.py / /post/1 /new-post /edit-post/1` | pass | GET /edit-post/1 -> 200 (local bootstrap css 200) |
| 68 | `../tools/flask_smoke.py / /register /login` | pass | GET /login -> 200 |
| 69 | `../tools/flask_smoke.py / /register /login /about` | pass | GET /about -> 200 (local bootstrap css 200) |
| 70 | `../tools/flask_smoke.py / /register /login` | pass | GET /login -> 200 (local bootstrap css 200) |

## GUI smoke tests (xvfb)

| Day | Command | Result | Last output line |
|---:|---|---|---|
| 18 | `-c "import turtle, main; turtle.tracer(0); main.paint(); ...` | pass |  |
| 18 | `-c "import turtle, exercises as e; turtle.tracer(0); turt...` | pass |  |
| 19 | `-c "import turtle, main; turtle.tracer(0); main.race('red...` | pass | You've lost! The purple turtle is the winner! |
| 19 | `-c "import etch_a_sketch as e; e.forwards(); e.turn_left(...` | pass |  |
| 20 | `-c "import turtle, main; main.main(max_frames=15); turtle...` | pass |  |
| 21 | `-c "import turtle, main; main.main(max_frames=40); turtle...` | pass |  |
| 22 | `-c "import turtle, main, pong; pong.Ball.move_speed=0; ma...` | pass |  |
| 23 | `-c "import turtle, main; main.main(max_frames=40); turtle...` | pass |  |
| 25 | `-c "import turtle, main; answers=iter(['Texas', 'ohio', '...` | pass | You got 2 states. The rest are in states_to_learn.csv |
| 27 | `main.py` | pass |  |
| 28 | `main.py` | pass |  |
| 29 | `main.py` | pass |  |
| 30 | `main.py` | pass |  |
| 31 | `main.py` | pass |  |
| 33 | `quote_app.py` | pass |  |
| 34 | `main.py` | pass |  |

## Selenium bots vs local mock sites (headless Chrome)

| Day | Command | Result | Last output line |
|---:|---|---|---|
| 48 | `main.py` | pass | Cookies per second: 12.0 after 30s |
| 48 | `exercises.py` | pass | Thanks for signing up! |
| 49 | `main.py` | pass | Done: 4 applied, 1 skipped. Server recorded 4 applications. |
| 50 | `main.py` | pass | Liked 20 profiles. |
| 51 | `main.py` | pass | Posted: Hey Internet Provider, why is my internet speed 71.97down/10.62up when I pay for 100down/20up? |
| 52 | `main.py` | pass | Followed 38 new accounts; now following 40 in total. |
| 53 | `main.py` | pass | Submitted 12 form responses -> responses.csv |

**Total failures: 0**
