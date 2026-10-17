"""Day 14 - Higher Lower: which account has more followers? (lists of dicts, game loop)."""
import random

from data import DATA


def describe(account: dict) -> str:
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def is_correct(guess: str, a: dict, b: dict) -> bool:
    return (guess == "a") == (a["follower_count"] > b["follower_count"])


def play(ask=input, rng=random) -> int:
    score = 0
    b = rng.choice(DATA)
    while True:
        a, b = b, rng.choice(DATA)
        while b is a:
            b = rng.choice(DATA)
        print(f"Compare A: {describe(a)}.\n  vs\nAgainst B: {describe(b)}.")
        guess = ask("Who has more followers? Type 'A' or 'B': ").strip().lower()
        if is_correct(guess, a, b):
            score += 1
            print(f"You're right! Current score: {score}.\n")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return score


if __name__ == "__main__":
    play()
