# Coffee Maker using OOP

from day16menu import Menu, MenuItem
from day16coffee_maker import CoffeeMaker
from day16money_machine import MoneyMachine

# Create object for the menu
coffee_menu = Menu()

# Create object for the coffee maker
coffee_maker = CoffeeMaker()

# Create transaction object
transaction = MoneyMachine()

# Turn the coffee maker on
coffeemakerison = True

while coffeemakerison:
    # Ask customer what whey want from the items available
    order = input(f"What would you like? {coffee_menu.get_items()} :").lower()

    # if order == off stop the program for machine maintenance
    if order == "off":
        coffeemakerison = False

    # if order == report show report of ingredients inventory and money
    elif order == "report":
        coffee_maker.report()
        transaction.report()

    # make the coffee
    else:
        # Get the MenuItem from the Menu and create drink object
        drink = coffee_menu.find_drink(order)
        # Check if resources are sufficient
        if coffee_maker.is_resource_sufficient(drink):
            # Get Payment
            if transaction.make_payment(drink.cost):
                # If payment sufficient for drink then make the coffee
                coffee_maker.make_coffee(drink)

    # Back to the beginning





