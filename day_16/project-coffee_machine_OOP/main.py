from coffee_maker import CoffeeMaker
from menu import Menu,MenuItem
from money_machine import MoneyMachine


coffee_maker_obj = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


cont = True
while(cont):
    customer_order = input(f"What would you like ? ({menu.get_items()})")
    if(customer_order=="report"):
        coffee_maker_obj.report()
        money_machine.report()

    elif(customer_order =="latte"or customer_order=="cappuccino" or customer_order=="espresso"):
        drink = menu.find_drink(customer_order)
        isResourceSufficient = coffee_maker_obj.is_resource_sufficient(drink)
        isPaymentSufficient = money_machine.make_payment(drink.cost)
        if(isPaymentSufficient and isPaymentSufficient):
            coffee_maker_obj.make_coffee(drink)


    else:
        print("Invalid request")
