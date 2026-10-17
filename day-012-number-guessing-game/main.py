"""Day 12 - Number Guessing Game: scope, global constants, functions returning values."""
import random

EASY_TURNS = 10
HARD_TURNS = 5


def check(guess: int, answer: int) -> str:
    if guess > answer:
        return "Too high."
    if guess < answer:
        return "Too low."
    return "correct"


def play(ask=input, rng=random) -> bool:
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    answer = rng.randint(1, 100)
    level = ask("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    turns = EASY_TURNS if level == "easy" else HARD_TURNS
    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(ask("Make a guess: "))
        result = check(guess, answer)
        if result == "correct":
            print(f"You got it! The answer was {answer}.")
            return True
        print(result)
        turns -= 1
    print(f"You've run out of guesses. The answer was {answer}.")
    return False


if __name__ == "__main__":
    play()
