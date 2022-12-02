from menu import Menu, MenuItem  
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

# Name Objects from Classes defined

money_machine = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()


# is resource sufficient in "coffee_maker and drink in menu class


machine_on = True

while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ( {options})\n")

    if choice == "off":
        machine_on = False
# Generates report from class
    elif choice == "report":
        coffeemaker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)

        if coffeemaker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)
