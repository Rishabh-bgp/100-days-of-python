"""Day 4 exercises: randomisation and lists."""
import random


def heads_or_tails(rng=random) -> str:
    return "Heads" if rng.randint(0, 1) == 1 else "Tails"


def banker_roulette(names: list[str], rng=random) -> str:
    return f"{rng.choice(names)} is going to buy the meal today!"


def treasure_map(position: str) -> list[list[str]]:
    """position like 'B3' = column B, row 3 on a 3x3 grid."""
    grid = [["⬜️"] * 3 for _ in range(3)]
    col = "ABC".index(position[0].upper())
    row = int(position[1]) - 1
    grid[row][col] = "X"
    return grid


if __name__ == "__main__":
    rng = random.Random(1)
    print(heads_or_tails(rng))
    print(banker_roulette(["Angela", "Ben", "Jenny", "Michael", "Chloe"], rng))
    for line in treasure_map("B3"):
        print(" ".join(line))
