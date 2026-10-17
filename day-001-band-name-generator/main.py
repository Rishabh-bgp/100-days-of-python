"""Day 1 - Band Name Generator: combine two answers into a band name."""


def band_name(city: str, pet: str) -> str:
    return f"{city.strip().title()} {pet.strip().title()}"


def main() -> None:
    print("Welcome to the Band Name Generator!")
    city = input("Which city did you grow up in?\n> ")
    pet = input("What is the name of a pet?\n> ")
    print(f"Your band name could be: {band_name(city, pet)}")


if __name__ == "__main__":
    main()
