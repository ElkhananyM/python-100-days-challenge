from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

while is_on:
    command = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if command == "off":
        is_on = False
    elif command == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(command)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)
