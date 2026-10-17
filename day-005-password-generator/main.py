"""Day 5 - PyPassword Generator using loops (and the secrets module for real randomness)."""
import secrets
import string

SYMBOLS = "!#$%&()*+"


def generate(n_letters: int, n_symbols: int, n_numbers: int) -> str:
    chars = (
        [secrets.choice(string.ascii_letters) for _ in range(n_letters)]
        + [secrets.choice(SYMBOLS) for _ in range(n_symbols)]
        + [secrets.choice(string.digits) for _ in range(n_numbers)]
    )
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def main() -> None:
    print("Welcome to the PyPassword Generator!")
    letters = int(input("How many letters would you like in your password?\n> "))
    symbols = int(input("How many symbols would you like?\n> "))
    numbers = int(input("How many numbers would you like?\n> "))
    print(f"Your password is: {generate(letters, symbols, numbers)}")


if __name__ == "__main__":
    main()
