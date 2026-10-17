"""Day 30 exercises: catching specific exceptions, raising your own."""


def safe_index(items: list, i: int):
    try:
        value = items[i]
    except IndexError:
        return "Index out of range"
    else:
        return value
    finally:
        pass  # runs no matter what


def count_likes(posts: list[dict]) -> int:
    total = 0
    for post in posts:
        try:
            total += post["Likes"]
        except KeyError:
            pass
    return total


def bmi(height: float, weight: float) -> float:
    if height > 3:
        raise ValueError("Human height should not be over 3 metres.")
    return weight / height ** 2


if __name__ == "__main__":
    print(safe_index(["Apple", "Pear", "Orange"], 5))
    print(count_likes([{"Likes": 21, "Comments": 2}, {"Comments": 1}, {"Likes": 19}]))
    try:
        bmi(45, 70)
    except ValueError as err:
        print("Caught:", err)
