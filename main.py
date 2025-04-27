from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    coffee_resources = CoffeeMaker()
    coffee_resources.report()
    money_payment = MoneyMachine()
    money_payment.report()
    coffee_menu = Menu()
    user_input = input(f"What would you like? ({coffee_menu.get_items()}): ")
    if user_input == "off":
        print("You switched off the coffee machine successfully.")
    elif user_input == "report":
        coffee_resources.report()
        money_payment.report()
    else:
        drink = coffee_menu.find_drink(user_input)
        if drink == None:
            coffee_machine()
        else:
            if coffee_resources.is_resource_sufficient(drink) == True and money_payment.make_payment(drink.cost) == True:
                    coffee_resources.make_coffee(drink)
                    coffee_resources.report()
                    money_payment.report()
            else:
                coffee_machine()

coffee_machine()