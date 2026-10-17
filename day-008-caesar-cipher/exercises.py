"""Day 8 exercises: functions with inputs."""
import math


def cans_needed(height: float, width: float, coverage: float = 5) -> int:
    return math.ceil(height * width / coverage)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


if __name__ == "__main__":
    print("Paint cans for 3x9 wall:", cans_needed(3, 9))
    print("Primes under 30:", [n for n in range(30) if is_prime(n)])
