"""Day 54 exercises: functions as first-class objects, nested functions and decorators,
including the 'speed calculator' decorator that times a function."""
import time
from functools import wraps


def delay_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        time.sleep(0.1)
        return function(*args, **kwargs)
    return wrapper


def speed_calc_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        print(f"{function.__name__} run speed: {time.perf_counter() - start:.4f}s")
        return result
    return wrapper


@delay_decorator
def say_hello() -> str:
    return "Hello"


@speed_calc_decorator
def fast_function() -> int:
    return sum(i * i for i in range(1_000_000))


@speed_calc_decorator
def slow_function() -> int:
    return sum(i * i for i in range(10_000_000))


if __name__ == "__main__":
    print(say_hello())
    fast_function()
    slow_function()
