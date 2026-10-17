"""Day 1 exercises: printing, debugging strings, input length, swapping variables."""


def print_lines() -> None:
    print("Day 1 - Python Print Function")
    print("The function is declared like this:")
    print("print('what to print')")


def name_length(name: str) -> int:
    return len(name)


def swap(a, b):
    a, b = b, a
    return a, b


if __name__ == "__main__":
    print_lines()
    print("Length of 'Rishabh':", name_length("Rishabh"))
    print("swap(3, 5) ->", swap(3, 5))
