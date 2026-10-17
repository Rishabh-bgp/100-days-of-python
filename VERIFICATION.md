# Verification report

Python 3.13.5; days 1-25.

## py_compile

51/51 files compile.

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
| 4 | `main.py` | pass | You win! |
| 4 | `exercises.py` | pass | ⬜️ X ⬜️ |
| 5 | `main.py` | pass | > Your password is: 32E2hWBn&fiq& |
| 5 | `exercises.py` | pass | 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz |
| 6 | `main.py` | pass | Reeborg reached the goal in 26 moves! |
| 6 | `exercises.py` | pass | Hurdles finished in 34 moves |
| 7 | `main.py` | pass | You lose! The word was 'galaxy'. |
| 8 | `main.py` | pass | > Goodbye |
| 8 | `exercises.py` | pass | Primes under 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] |
| 9 | `main.py` | pass | The winner is Ben with a bid of $150.00 |
| 9 | `exercises.py` | pass | [{'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']}, {'country': 'India', 'visits': 3, 'cities': ['Delhi', 'Bhopal'] |
| 10 | `main.py` | pass | Type 'y' to continue with 4.0, 'n' to start again, or 'q' to quit: |
| 10 | `exercises.py` | pass | Feb 2024 has 29 days |
| 11 | `main.py` | pass | Do you want to play a game of Blackjack? Type 'y' or 'n': |
| 12 | `main.py` | pass | You've run out of guesses. The answer was 13. |
| 12 | `exercises.py` | pass | 73 It's a prime number. |
| 13 | `exercises.py` | pass | even ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'] |
| 14 | `main.py` | pass | Who has more followers? Type 'A' or 'B': Sorry, that's wrong. Final score: 0 |
| 15 | `main.py` | pass | What would you like? (espresso/latte/cappuccino): Turning off. Goodbye! |
| 16 | `main.py` | pass | What would you like? (latte/espresso/cappuccino): |
| 16 | `exercises.py` | pass | +--------------+----------+ |
| 17 | `main.py` | pass | You've completed the quiz. Final score: 7/12 |
| 24 | `main.py` | pass | Wrote 7 letters to Output/ReadyToSend/ |
| 24 | `exercises.py` | pass | absolute path example: /tmp/tmpkuw8pl7v/data.txt |
| 25 | `exercises.py` | pass | 2     Black    146 |
| 25 | `-c "import main; d=main.load_states(); print(main.check_g...` | pass | 49 |

## Flask test-client checks

| Day | Command | Result | Last output line |
|---:|---|---|---|

## GUI smoke tests (xvfb)

| Day | Command | Result | Last output line |
|---:|---|---|---|
| 18 | `-c "import turtle, main; turtle.tracer(0); main.paint(); ...` | pass |  |
| 18 | `-c "import turtle, exercises as e; turtle.tracer(0); turt...` | pass |  |
| 19 | `-c "import turtle, main; turtle.tracer(0); main.race('red...` | pass | You've lost! The green turtle is the winner! |
| 19 | `-c "import etch_a_sketch as e; e.forwards(); e.turn_left(...` | pass |  |
| 20 | `-c "import turtle, main; main.main(max_frames=15); turtle...` | pass |  |
| 21 | `-c "import turtle, main; main.main(max_frames=40); turtle...` | pass |  |
| 22 | `-c "import turtle, main, pong; pong.Ball.move_speed=0; ma...` | pass |  |
| 23 | `-c "import turtle, main; main.main(max_frames=40); turtle...` | pass |  |

**Total failures: 0**
