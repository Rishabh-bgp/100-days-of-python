"""Classes for the OOP coffee machine (original implementation)."""
from dataclasses import dataclass, field


@dataclass
class MenuItem:
    name: str
    cost: float
    water: int
    milk: int = 0
    coffee: int = 0

    @property
    def ingredients(self) -> dict[str, int]:
        return {"water": self.water, "milk": self.milk, "coffee": self.coffee}


class Menu:
    def __init__(self) -> None:
        self.items = [
            MenuItem("latte", 2.5, water=200, milk=150, coffee=24),
            MenuItem("espresso", 1.5, water=50, coffee=18),
            MenuItem("cappuccino", 3.0, water=250, milk=50, coffee=24),
        ]

    def get_items(self) -> str:
        return "/".join(i.name for i in self.items)

    def find_drink(self, name: str) -> MenuItem | None:
        for item in self.items:
            if item.name == name:
                return item
        print("Sorry that item is not available.")
        return None


@dataclass
class CoffeeMaker:
    resources: dict[str, int] = field(default_factory=lambda: {"water": 300, "milk": 200, "coffee": 100})

    def report(self) -> None:
        print(f"Water: {self.resources['water']}ml\nMilk: {self.resources['milk']}ml\nCoffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink: MenuItem) -> bool:
        for k, v in drink.ingredients.items():
            if v > self.resources[k]:
                print(f"Sorry there is not enough {k}.")
                return False
        return True

    def make_coffee(self, drink: MenuItem) -> None:
        for k, v in drink.ingredients.items():
            self.resources[k] -= v
        print(f"Here is your {drink.name} ☕️. Enjoy!")


class MoneyMachine:
    COINS = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    def __init__(self, ask=input) -> None:
        self.profit = 0.0
        self.ask = ask

    def report(self) -> None:
        print(f"Money: ${self.profit:.2f}")

    def make_payment(self, cost: float) -> bool:
        print("Please insert coins.")
        received = sum(int(self.ask(f"How many {c}?: ") or 0) * v for c, v in self.COINS.items())
        if received >= cost:
            change = round(received - cost, 2)
            if change:
                print(f"Here is ${change:.2f} in change.")
            self.profit += cost
            return True
        print("Sorry that's not enough money. Money refunded.")
        return False
