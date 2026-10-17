"""Day 16 - OOP Coffee Machine: using classes, objects, attributes and methods."""
from coffee import CoffeeMaker, Menu, MoneyMachine


def run(ask=input) -> None:
    menu, maker, money = Menu(), CoffeeMaker(), MoneyMachine(ask)
    while True:
        choice = ask(f"What would you like? ({menu.get_items()}): ").strip().lower()
        if choice == "off":
            return
        if choice == "report":
            maker.report()
            money.report()
            continue
        drink = menu.find_drink(choice)
        if drink and maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            maker.make_coffee(drink)


if __name__ == "__main__":
    run()
