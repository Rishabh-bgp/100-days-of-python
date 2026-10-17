"""Typing-test maths, kept separate from the GUI so it can be tested."""
import random

SENTENCES = [
    "The quick brown fox jumps over the lazy dog near the quiet river bank.",
    "Practice a little every day and your typing speed will grow steadily.",
    "Python makes it easy to turn a small idea into a working program.",
    "Clear names and short functions make code easier to read and change.",
    "A good test checks one thing and tells you exactly what went wrong.",
]


def pick_sentence(rng=random) -> str:
    return rng.choice(SENTENCES)


def score(target: str, typed: str, seconds: float) -> dict:
    """WPM uses the standard 5 characters = 1 word; accuracy compares character by character."""
    seconds = max(seconds, 0.001)
    correct = sum(1 for a, b in zip(target, typed) if a == b)
    accuracy = correct / max(len(target), 1)
    gross_wpm = (len(typed) / 5) / (seconds / 60)
    return {"wpm": round(gross_wpm, 1), "net_wpm": round(gross_wpm * accuracy, 1), "accuracy": round(accuracy * 100, 1)}
