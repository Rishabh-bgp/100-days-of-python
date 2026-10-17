"""Day 7 - Hangman: while loops, lists, string methods."""
import random

from words import STAGES, WORDS


def play(word: str, ask=input, say=print) -> bool:
    lives = len(STAGES) - 1
    guessed: set[str] = set()
    while lives > 0:
        display = " ".join(c if c in guessed else "_" for c in word)
        say(f"\n{display}   lives: {lives}")
        if "_" not in display:
            say("You win!")
            return True
        try:
            guess = ask("Guess a letter: ").strip().lower()[:1]
        except EOFError:
            say("\nNo more input - quitting.")
            return False
        if not guess.isalpha():
            say("Please type a letter.")
            continue
        if guess in guessed:
            say(f"You've already guessed {guess}.")
            continue
        guessed.add(guess)
        if guess not in word:
            lives -= 1
            say(f"'{guess}' is not in the word. You lose a life.")
        say(STAGES[len(STAGES) - 1 - lives])
    say(f"You lose! The word was '{word}'.")
    return False


if __name__ == "__main__":
    play(random.choice(WORDS))
