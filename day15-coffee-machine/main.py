MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# TODO 1: Print status report of all coffee machine resources.
def print_report():
    """Prints a status report of the machine's reserves of water, milk, coffe, and stored money."""
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")


# TODO 2: Check resources sufficient?
def check_resources(customer_order, machine_resources):
    """Checks whether the machine has enough resources to make the customer's order."""
    if customer_order == "espresso":
        resources_state = "False" if machine_resources["water"] < 50 or machine_resources["coffee"] < 18 else "True"
    else:
        resources_state = "False" if machine_resources["water"] < MENU[customer_order]["ingredients"]["water"] or \
                                     machine_resources["milk"] < MENU[customer_order]["ingredients"]["milk"] or \
                                     machine_resources["coffee"] < MENU[customer_order]["ingredients"][
                                         "coffee"] else "True"
    return resources_state


# TODO 3: Process coins.
def process_coins():
    """Asks the user to insert coins before processing their order."""
    print("Please insert coins.")
    try:
        customer_quarters = QUARTER * float(input("How many quarters? "))
        customer_dimes = DIME * float(input("How many dimes? "))
        customer_nickles = NICKLE * float(input("How many nickles? "))
        customer_pennies = PENNY * float(input("How many pennies? "))
    except ValueError:
        print("Invalid number entered")
    return customer_quarters + customer_dimes + customer_nickles + customer_pennies


# TODO 4: Check transaction success.
def process_payment(coins):
    """Processes the payment and confirms that the user put sufficient coins in the machine."""
    if coins < MENU[user_command]["cost"]:
        return False
    else:
        print(f"Here's your change: ${coins:.2f} - ${MENU[user_command]["cost"]} = ${coins - MENU[user_command]["cost"]:.2f}")


# TODO 5: Make coffee and update resources.
def make_coffee(coffee_type):
    """Produces the coffee, and updates the resources the machine has left after the order is fulfilled."""
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    if coffee_type == "latte" or coffee_type == "cappuccino":
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["money"] += MENU[user_command]["cost"]


PENNY = 0.01
NICKLE = 0.05
DIME = 0.10
QUARTER = 0.25
while True:
    try:
        user_command = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_command == "status":
            print_report()
            continue
        if user_command == "off":
            print("Have a nice day! Goodbye.")
            break
        if check_resources(user_command, resources) == "False":
            print("Sorry, there is not enough resources to make your drink!")
            continue
        try:
            coins_deposited = process_coins()
        except UnboundLocalError:
            continue
        confirm_payment = process_payment(coins_deposited)
        if confirm_payment == False:
            print("Sorry that's not enough money. Money refunded.")
            continue
        make_coffee(user_command)
        print(f"Here's your {user_command}. Enjoy!")
    except KeyError:
        print("Invalid command! Please enter a valid command.\n'espresso'\n'latte'\n'cappuccino'\n'status'\n'off'")
        continue