"""Day 26 - NATO Alphabet: list & dictionary comprehensions (plus Day 30's KeyError handling)."""
import csv
from pathlib import Path

HERE = Path(__file__).parent


def load_alphabet() -> dict[str, str]:
    with open(HERE / "nato_phonetic_alphabet.csv", newline="") as fh:
        return {row["letter"]: row["code"] for row in csv.DictReader(fh)}


def spell(word: str, alphabet: dict[str, str]) -> list[str]:
    return [alphabet[ch] for ch in word.upper() if not ch.isspace()]


def main(ask=input) -> None:
    alphabet = load_alphabet()
    while True:
        try:
            word = ask("Enter a word: ")
        except EOFError:
            return
        try:
            print(spell(word, alphabet))
            return
        except KeyError:
            print("Sorry, only letters in the alphabet please.")


if __name__ == "__main__":
    main()
