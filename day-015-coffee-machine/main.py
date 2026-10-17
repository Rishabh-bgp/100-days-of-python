"""Day 15 - Coffee Machine (procedural): dictionaries, functions, a REPL loop."""
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}
COINS = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}


def missing(resources: dict, ingredients: dict) -> list[str]:
    return [k for k, v in ingredients.items() if resources.get(k, 0) < v]


def process_coins(ask=input) -> float:
    print("Please insert coins.")
    return sum(int(ask(f"How many {name}?: ") or 0) * value for name, value in COINS.items())


def run(ask=input) -> None:
    resources = {"water": 300, "milk": 200, "coffee": 100}
    profit = 0.0
    while True:
        choice = ask("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if choice == "off":
            print("Turning off. Goodbye!")
            return
        if choice == "report":
            for k, unit in (("water", "ml"), ("milk", "ml"), ("coffee", "g")):
                print(f"{k.title()}: {resources[k]}{unit}")
            print(f"Money: ${profit:.2f}")
            continue
        if choice not in MENU:
            print("Sorry, that's not on the menu.")
            continue
        drink = MENU[choice]
        short = missing(resources, drink["ingredients"])
        if short:
            print(f"Sorry there is not enough {', '.join(short)}.")
            continue
        paid = process_coins(ask)
        if paid < drink["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            continue
        if paid > drink["cost"]:
            print(f"Here is ${paid - drink['cost']:.2f} in change.")
        profit += drink["cost"]
        for k, v in drink["ingredients"].items():
            resources[k] -= v
        print(f"Here is your {choice} ☕️. Enjoy!")


if __name__ == "__main__":
    run()
