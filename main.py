from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeMaker = CoffeeMaker()
menu = Menu()
moneyProcess = MoneyMachine()

should_continue = True

while should_continue:
    item = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if item == "report":
        coffeMaker.report()
    else:
        flag = coffeMaker.is_resource_sufficient(menu.find_drink(item))
        if flag:
            is_payment_successful = moneyProcess.make_payment(menu.find_drink(item).cost)
            if is_payment_successful:
                coffeMaker.make_coffee(menu.find_drink(item))

