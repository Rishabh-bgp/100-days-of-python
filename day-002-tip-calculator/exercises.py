"""Day 2 exercises: data types, number manipulation, f-strings."""


def add_digits(two_digit: str) -> int:
    """Add the two digits of a two-digit number given as a string."""
    return int(two_digit[0]) + int(two_digit[1])


def bmi(height_m: float, weight_kg: float) -> int:
    return int(weight_kg / height_m ** 2)


def life_in_weeks(age: int, lifespan: int = 90) -> str:
    weeks_left = (lifespan - age) * 52
    return f"You have {weeks_left} weeks left."


if __name__ == "__main__":
    print("add_digits('39') =", add_digits("39"))
    print("bmi(1.75, 80) =", bmi(1.75, 80))
    print(life_in_weeks(25))
