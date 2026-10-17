"""Day 3 exercises: conditionals, logical operators, nesting."""


def odd_or_even(n: int) -> str:
    return "even" if n % 2 == 0 else "odd"


def bmi_category(height_m: float, weight_kg: float) -> str:
    value = round(weight_kg / height_m ** 2)
    if value < 18.5:
        label = "underweight"
    elif value < 25:
        label = "normal weight"
    elif value < 30:
        label = "slightly overweight"
    elif value < 35:
        label = "obese"
    else:
        label = "clinically obese"
    return f"Your BMI is {value}, you are {label}."


def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def pizza_price(size: str, pepperoni: bool, extra_cheese: bool) -> int:
    prices = {"S": 15, "M": 20, "L": 25}
    total = prices[size.upper()]
    if pepperoni:
        total += 2 if size.upper() == "S" else 3
    if extra_cheese:
        total += 1
    return total


def love_score(name1: str, name2: str) -> int:
    combined = (name1 + name2).lower()
    true_count = sum(combined.count(c) for c in "true")
    love_count = sum(combined.count(c) for c in "love")
    return int(f"{true_count}{love_count}")


def love_message(score: int) -> str:
    if score < 10 or score > 90:
        return f"Your score is {score}, you go together like coke and mentos."
    if 40 <= score <= 50:
        return f"Your score is {score}, you are alright together."
    return f"Your score is {score}."


if __name__ == "__main__":
    print("7 is", odd_or_even(7))
    print(bmi_category(1.8, 85))
    print("2000 leap?", is_leap(2000), "| 1900 leap?", is_leap(1900))
    print("Large pizza with pepperoni + cheese: $", pizza_price("L", True, True))
    s = love_score("Angela Yu", "Jack Bauer")
    print(love_message(s))
