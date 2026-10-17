"""Day 10 - Calculator: functions with outputs, functions stored in a dict."""
import operator

OPERATIONS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def calculate(a: float, op: str, b: float) -> float:
    return OPERATIONS[op](a, b)


def main() -> None:
    result = float(input("What's the first number?: "))
    while True:
        print(" ".join(OPERATIONS))
        op = input("Pick an operation: ").strip()
        b = float(input("What's the next number?: "))
        try:
            new = calculate(result, op, b)
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            continue
        except KeyError:
            print("Unknown operation.")
            continue
        print(f"{result} {op} {b} = {new}")
        result = new
        choice = input(f"Type 'y' to continue with {result}, 'n' to start again, or 'q' to quit: ").strip().lower()
        if choice == "n":
            result = float(input("What's the first number?: "))
        elif choice != "y":
            break


if __name__ == "__main__":
    main()
