COFFEE_MENU = {
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

COFFEE_MACHINE_RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def display_coffee_machine_report():
    """This function displays the coffee machine report."""
    print(f"Water: {COFFEE_MACHINE_RESOURCES['water']}ml")
    print(f"Milk: {COFFEE_MACHINE_RESOURCES['milk']}ml")
    print(f"Coffee: {COFFEE_MACHINE_RESOURCES['coffee']}g")


def accept_coins_and_calculate_total():
    """This function accepts coins from the user and calculates the total amount inserted."""
    print("Please Insert Coins.\n")
    num_quarters = int(input("How many quarters:"))
    num_dimes = int(input("How many dimes:"))
    num_nickles = int(input("How many nickles:"))
    num_pennies = int(input("How many pennies:"))
    return 0.25 * num_quarters + 0.1 * num_dimes + 0.05 * num_nickles + 0.01 * num_pennies


def serve_coffee_and_return_change(total_inserted_coins, selected_coffee):
    """This function serves the coffee and returns the change to the user."""
    change = total_inserted_coins - COFFEE_MENU[selected_coffee]["cost"]
    print(f"Here is your change ${change:.2f}.\n")
    print(f"Here is your {selected_coffee} ☕ Enjoy!")


def are_resources_sufficient_for_selected_coffee(selected_coffee):
    """This function checks if the coffee machine has sufficient resources to make the selected coffee."""
    for item in COFFEE_MENU[selected_coffee]["ingredients"]:
        if COFFEE_MACHINE_RESOURCES[item] < COFFEE_MENU[selected_coffee]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    else:
        return True


def process_coffee_order(selected_coffee):
    """This function processes the coffee order and returns True if the coffee is processed successfully."""
    coffee_processed = False
    if are_resources_sufficient_for_selected_coffee(selected_coffee):
        total_inserted_coins = accept_coins_and_calculate_total()
        if total_inserted_coins >= COFFEE_MENU[selected_coffee]["cost"]:
            serve_coffee_and_return_change(total_inserted_coins, selected_coffee)
            coffee_processed = True
        else:
            print("Sorry that's not enough money. Money refunded.")
    return coffee_processed


def update_coffee_machine_resources(selected_coffee):
    """This function updates the coffee machine resources after a coffee is served."""
    for item in COFFEE_MENU[selected_coffee]["ingredients"]:
        COFFEE_MACHINE_RESOURCES[item] -= COFFEE_MENU[selected_coffee]["ingredients"][item]


print("Welcome to the coffee machine!")


def coffee_machine():
    """This function is the main function that runs the coffee machine."""
    coffee_machine_on = True
    while coffee_machine_on:
        user_selection = input("What would you like? (espresso/latte/cappuccino):").lower()
        if user_selection == "report":
            display_coffee_machine_report()
        elif user_selection == "off":
            print("Coffee machine is shutting down.")
            coffee_machine_on = False
        else:
            if process_coffee_order(user_selection):
                update_coffee_machine_resources(user_selection)


coffee_machine()
