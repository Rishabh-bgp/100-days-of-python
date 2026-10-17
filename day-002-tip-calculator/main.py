"""Day 2 - Tip Calculator: split a bill including tip between people."""


def per_person(bill: float, tip_percent: float, people: int) -> float:
    if people <= 0:
        raise ValueError("people must be at least 1")
    return round(bill * (1 + tip_percent / 100) / people, 2)


def main() -> None:
    print("Welcome to the tip calculator!")
    bill = float(input("What was the total bill? $"))
    tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))
    print(f"Each person should pay: ${per_person(bill, tip, people):.2f}")


if __name__ == "__main__":
    main()
