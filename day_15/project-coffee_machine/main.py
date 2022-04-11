import data

resource = data.resources
menu = data.MENU


def report(resource_in, profit):
    for key, value in resource_in.items():
        if key == "Coffee":
            print(f"{key}: {value}ml")
        else:
            print(f"{key}: {value}g")
    print(f"Money: ${profit}")


def getCoinFromUser():
    print("Please insert coins.")
    num_quarter = int(input("How many quarters?"))
    num_dimes = int(input("How many dimes?"))
    num_nickel = int(input("How many nickels?"))
    num_pennies = int(input("How many pennies?"))
    total = ((num_pennies * 0.01) + (num_nickel * 0.05) + (num_dimes * 0.1) + (num_quarter * 0.25))
    return round(total, 2)


def resourceAdjustment(local_resource, selected_drink):
    resource_in = local_resource
    for ingredient, value in menu[selected_drink]["ingredients"].items():
        resource_in[ingredient] = local_resource[ingredient] - value
    return resource_in


def isEnoughChange(total, selected_drink):
    if total >= menu[selected_drink]["cost"]:
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def isEnoughResource(local_resource, selected_drink):
    for ingredient, value in menu[selected_drink]["ingredients"].items():
        if local_resource[ingredient] < value:
            print(f"Sorry there is not enough {ingredient}")
            return False

    return True


def getChange(total_coin, drink):
    drink_price = menu[drink]["cost"]
    print(f"Here is ${round(total_coin - drink_price, 3)} in change.")
    print(f"Here is your {drink} Enjoy")


'''
Logic of the coffer machine
'''
cont = True
money = 0
while cont:

    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        report(resource, money)
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        total_change = getCoinFromUser()
        isValidChange = isEnoughChange(total_change, user_input)
        isValidResource = isEnoughResource(resource, user_input)
        if isValidResource and isValidChange:
            resource = resourceAdjustment(resource, user_input)
            getChange(total_change, user_input)
            money += menu[user_input]["cost"]
    else:
        print("Invalid input, please try again")
        cont = False
