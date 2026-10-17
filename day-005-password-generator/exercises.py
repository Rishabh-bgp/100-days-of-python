"""Day 5 exercises: for loops and range (written without sum()/max() on purpose)."""


def average_height(heights: list[int]) -> int:
    total = 0
    count = 0
    for h in heights:
        total += h
        count += 1
    return round(total / count)


def high_score(scores: list[int]) -> int:
    best = scores[0]
    for s in scores:
        if s > best:
            best = s
    return best


def add_evens(limit: int = 100) -> int:
    total = 0
    for n in range(2, limit + 1, 2):
        total += n
    return total


def fizzbuzz(limit: int = 100) -> list[str]:
    out = []
    for n in range(1, limit + 1):
        if n % 15 == 0:
            out.append("FizzBuzz")
        elif n % 3 == 0:
            out.append("Fizz")
        elif n % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(n))
    return out


if __name__ == "__main__":
    print("Average height:", average_height([180, 124, 165, 173, 189, 169, 146]))
    print("High score:", high_score([78, 65, 89, 86, 55, 91, 64, 89]))
    print("Sum of evens to 100:", add_evens())
    print(" ".join(fizzbuzz(15)))
