
# Dictionary of machine resources
machine_resources = {"water": 1000, "milk": 2000, "coffee": 500, "money": 0 }

# Dictionary of coffee types
coffee_menu = {"latte": {"water": 250, "milk": 100, "coffee": 14, "cost": 2.50},
         "cappuccino": {"water": 200, "milk": 150, "coffee": 24, "cost": 3.00 },
         "expresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.50 },
               }


def report_resources():
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g")
    print(f"Money: ${round(machine_resources['money'], 2):.2f}")


def check_resources(order_resource):
    # print(order)
    for resource in machine_resources:
        if resource != "money" and machine_resources[resource] < coffee_menu[order_resource][resource]:
            print(f"Sorry there is not enough {resource}")
            return False
    return True


def process_coins(pay_order):
    print(f"A {pay_order} cost ${round(coffee_menu[pay_order]['cost'], 2):.2f}. Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = (0.25 * quarters) + (.10 * dimes) + (.05 * nickles) + (.01 * pennies)

    if total < coffee_menu[pay_order]["cost"]:
        print(f"Sorry that's not enough money. Refunding ${round(total, 2):.2f}")
        return False
    elif total > coffee_menu[pay_order]["cost"]:
        print(f"That was too much money. A {order} cost ${round(coffee_menu[pay_order]['cost'], 2):.2f}, your refund is ${round(total - coffee_menu[pay_order]['cost'], 2):.2f}")

    return True


def deduct_resources(deduct_order):
    machine_resources['water'] = machine_resources['water'] - coffee_menu[deduct_order]['water']
    machine_resources['milk'] = machine_resources['milk'] - coffee_menu[deduct_order]['milk']
    machine_resources['coffee'] = machine_resources['coffee'] - coffee_menu[deduct_order]['coffee']
    machine_resources['money'] = machine_resources['money'] + coffee_menu[deduct_order]['cost']
    return True


def make_coffee(coffee_order):
    make_order = True
    # Check if resources are sufficient (water, milk, coffee)
    make_order = check_resources(coffee_order)
    # Process coins
    if make_order:
        make_order = process_coins(coffee_order)

    # Deduct resources
    if make_order:
        print(f"Making your {coffee_order}")
        make_order = deduct_resources(coffee_order)

    # transaction good
    if make_order:
        print(f"Here is your {coffee_order}. Enjoy!")


coffee_ops = True

while coffee_ops:

    # Prompt user "What would you like? (expresso,latte,cappuccino)"
    order = input("What would you like? (expresso,latte,cappuccino): ").lower()

    # Turn off the Coffee machine by entering off at the prompt
    if order == "off":
        coffee_ops = False
    elif order == "report":
        # Print report of resources if report is entered at prompt
        report_resources()
    else:
        make_coffee(order)


print("Coffee Maker Shutdown for Maintenance.")