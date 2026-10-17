"""Day 4 - Rock Paper Scissors against the computer (random module, lists)."""
import random

CHOICES = ["Rock", "Paper", "Scissors"]
ART = [
    "    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)",
    "    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)",
    "    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)",
]


def winner(user: int, computer: int) -> str:
    if user == computer:
        return "draw"
    return "win" if (user - computer) % 3 == 1 else "lose"


def main(rng=random) -> None:
    raw = input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n> ").strip()
    if raw not in {"0", "1", "2"}:
        print("Invalid choice, you lose!")
        return
    user = int(raw)
    computer = rng.randint(0, 2)
    print(f"You chose {CHOICES[user]}:\n{ART[user]}")
    print(f"Computer chose {CHOICES[computer]}:\n{ART[computer]}")
    print({"draw": "It's a draw.", "win": "You win!", "lose": "You lose."}[winner(user, computer)])


if __name__ == "__main__":
    main()
