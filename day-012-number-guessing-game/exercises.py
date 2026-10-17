"""Day 12 exercises: local vs global scope."""
enemies = 1


def increase_enemies_local() -> int:
    enemies = 2  # a new local name; the global is untouched
    return enemies


def increase_enemies(current: int) -> int:
    """Preferred: take the value in, return the new value (no 'global')."""
    return current + 1


def prime_checker(n: int) -> str:
    is_prime = n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
    return "It's a prime number." if is_prime else "It's not a prime number."


if __name__ == "__main__":
    print("local:", increase_enemies_local(), "global still:", enemies)
    enemies = increase_enemies(enemies)
    print("after returning a new value:", enemies)
    print(73, prime_checker(73))
