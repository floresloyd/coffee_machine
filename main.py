from data import MENU, resources


def get_report(dictionary):
    """ Prints out contents of a dictionary """
    for key in dictionary:
        print(key, f": {resources[key]}")


def coin_counter():
    """ Tallies number of coins and returns total value """
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    quarters_amt = quarters * .25
    dimes_amt = dimes * .10
    nickles_amt = nickles * .05
    pennies_amt = pennies * .01
    total_coins_amt = round(quarters_amt + dimes_amt + nickles_amt + pennies_amt, 2)
    return total_coins_amt


def transact(a, b):
    """ Takes money and cost and determines if you have enough money, returns change if so."""
    if a > b:
        change = round(a - b, 2)
        print(f"Here is ${change} in change.")
        return change
    else:
        change = 0
        print("Sorry that's not enough money. Money refunded.")
        return change


def check_resources(order, supply):
    """ Checks if we have sufficient supply to produce an order"""
    """ Returns True if we have enough, false if we don't"""
    enough_resources = True
    counter = 0
    # TRANSFERS elements of [order]& [supply] to an array
    a = []
    b = []
    # TO_UPDATE : FOR LOOP DOES NOT WORK FOR NESTED DICTIONARY KEEPS GIVING KEY ERROR
    a.append(MENU[order]["ingredients"]["water"])
    a.append(MENU[order]["ingredients"]["milk"])
    a.append(MENU[order]["ingredients"]["coffee"])
    for key in supply:
        b.append(resources[key])
    b.pop(3)                         # removes money from array b
    # print(a)                       # prints array a & b to check transfer : FOR TESTING
    # print(b)
    for i in range(0, 3):            # compares each index of two arrays
        if a[i] < b[i]:
            counter += 1             # if a[i] < b[i]; it means we have enough of that resource
    if counter < 3:
        enough_resources = False     # we don't have enough ingredients
        print("Sorry there is not enough ingredients.")
    # print(counter)                  # PRINTS COUNTER : FOR TESTING
    # print(enough_resources)         # PRINTS T/F     : FOR TESTING
    return enough_resources


# def calculate_depleted_resources(drink):
#     """ Takes in the drink selected and returns an array of the cost of [water, milk, coffee]"""
#     resources_used = [MENU[drink]["ingredients"]["water"], MENU[drink]["ingredients"]["milk"],
#                       MENU[drink]["ingredients"]["coffee"]]
#     return resources_used


def refill():
    """ REFILLS OUR MACHINE BACK TO STOCK"""
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    print("MACHINE REFILLED!")


def coffee_machine():
    is_on = True
    while is_on:
        selected_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if selected_drink == "report":
            get_report(resources)
        elif selected_drink == "espresso":
            if check_resources(selected_drink, resources):
                payment_received = coin_counter()                   # total money
                cost_of_drink = MENU[selected_drink]["cost"]        # total cost
                if transact(payment_received, cost_of_drink) > 0:   # If you have enough continue, if not RE-LOOP TO 65
                    print("TRANSACTED")
                    print(f"Here is your espresso! Enjoy <3")
                    # ONCE TRANSACTED WE UPDATE OUR RESOURCES
                    resources["money"] += cost_of_drink  # update profits in [resources]
                    resources["water"] -= MENU[selected_drink]["ingredients"]["water"]
                    resources["milk"] -= MENU[selected_drink]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[selected_drink]["ingredients"]["coffee"]
                    # TO IMPLEMENT : MORE EFFICIENT WAY TO UPDATE CONSUMED GOODS
                    # resources_consumed = calculate_depleted_resources(selected_drink)
                else:
                    coffee_machine()                    # IF WE DON'T HAVE MONEY
            else:
                coffee_machine()                        # IF WE DON'T HAVE ENOUGH RESOURCES
        elif selected_drink == "latte":
            if check_resources(selected_drink, resources):
                payment_received = coin_counter()
                cost_of_drink = MENU[selected_drink]["cost"]
                if transact(payment_received, cost_of_drink) > 0:
                    print("TRANSACTED")
                    print(f"Here is your latte! Enjoy <3")
                    # ONCE TRANSACTED WE UPDATE OUR RESOURCES
                    resources["money"] += cost_of_drink  # update profits in [resources]
                    resources["water"] -= MENU[selected_drink]["ingredients"]["water"]
                    resources["milk"] -= MENU[selected_drink]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[selected_drink]["ingredients"]["coffee"]
                else:
                    coffee_machine()                    # IF WE DON'T HAVE MONEY
            else:
                coffee_machine()                        # IF WE DON'T HAVE ENOUGH RESOURCES
        elif selected_drink == "cappuccino":
            if check_resources(selected_drink, resources):
                payment_received = coin_counter()
                cost_of_drink = MENU[selected_drink]["cost"]
                if transact(payment_received, cost_of_drink) > 0:
                    print("TRANSACTED")
                    print(f"Here is your cappuccino! Enjoy <3")
                    # ONCE TRANSACTED WE UPDATE OUR RESOURCES
                    resources["money"] += cost_of_drink  # update profits in [resources]
                    resources["water"] -= MENU[selected_drink]["ingredients"]["water"]
                    resources["milk"] -= MENU[selected_drink]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[selected_drink]["ingredients"]["coffee"]
                else:
                    coffee_machine()                    # IF WE DON'T HAVE MONEY
            else:
                coffee_machine()                        # IF WE DON'T HAVE ENOUGH RESOURCES
        elif selected_drink == "check":
            print("OTHER DRINK")
        elif selected_drink == "off":
            print("POWER OFF!")
            is_on = False
        elif selected_drink == "refill":
            refill()
        else:
            print("INVALID SELECTION TRY AGAIN!")
            coffee_machine()


coffee_machine()