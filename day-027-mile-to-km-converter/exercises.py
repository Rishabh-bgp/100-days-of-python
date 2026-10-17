"""Day 27 exercises: default arguments, *args and **kwargs."""


def add(*args: float) -> float:
    total = 0
    for n in args:
        total += n
    return total


def calculate(n: float, **kwargs: float) -> float:
    n += kwargs.get("add", 0)
    n *= kwargs.get("multiply", 1)
    return n


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")


if __name__ == "__main__":
    print(add(3, 5, 6, 2, 1, 7, 4, 3))
    print(calculate(2, add=3, multiply=5))
    car = Car(make="Tata")
    print(car.make, car.model)
