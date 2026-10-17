"""Day 10 exercises: functions that return values."""


def format_name(first: str, last: str) -> str:
    if not first or not last:
        return "You didn't provide valid inputs."
    return f"{first.title()} {last.title()}"


def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year: int, month: int) -> int:
    if not 1 <= month <= 12:
        raise ValueError("month must be 1-12")
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    return days[month - 1]


if __name__ == "__main__":
    print(format_name("rIsHaBh", "ARYAN"))
    print("Feb 2024 has", days_in_month(2024, 2), "days")
