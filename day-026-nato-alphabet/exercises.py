"""Day 26 exercises: comprehensions."""


def squares(numbers: list[int]) -> list[int]:
    return [n * n for n in numbers]


def evens(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]


def overlap(a: list[int], b: list[int]) -> list[int]:
    return [n for n in a if n in b]


def word_lengths(sentence: str) -> dict[str, int]:
    return {w: len(w) for w in sentence.split()}


def to_fahrenheit(weather_c: dict[str, float]) -> dict[str, float]:
    return {day: c * 9 / 5 + 32 for day, c in weather_c.items()}


if __name__ == "__main__":
    print(squares([1, 1, 2, 3, 5, 8]))
    print(evens([1, 1, 2, 3, 5, 8, 13, 21, 34, 55]))
    print(overlap([3, 6, 5, 8, 33, 12], [12, 3, 5, 6, 13, 8]))
    print(word_lengths("What is the Airspeed Velocity of an Unladen Swallow?"))
    print(to_fahrenheit({"Monday": 12, "Tuesday": 14, "Wednesday": 15}))
