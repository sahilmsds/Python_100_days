import math
import os

MENU = {
    "espresso": {
        "ingredients":{
            "water": 50,
            "coffee": 18
        },
        "cost":1.5
    },
    "latte": {
        "ingredients":{
            "water":200,
            "coffee":24,
            "milk":150
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "coffee":24,
            "milk":100
        },
        "cost":3
    }
}

resources = {
    "water":300,
    "milk":200,
    "coffee":100
}
money = 0

def check_resources(drink):
    for item in drink["ingredients"]:
        if resources[item] < drink["ingredients"][item]:
            print("Not enough resources in machine")
            return False
    return True
    
def coffee_machine(drink):
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]


def check_payment(drink, user_amount):
    if user_amount >= drink["cost"]:
        remaining = round(user_amount - drink["cost"], 2)
        if remaining > 0:
            return True, f"Here is ${remaining} in change."
        else:
            return True, "Payment Accepted."
    else:
        return False, "Not enough Money"
    
def refill():
    resources["coffee"] += 100
    resources["milk"]+= 200
    resources["water"] += 300
machine_is_on = True
while machine_is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        print(f'Report\nWater: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${money}')
        input("press ENTER to continue....")
        os.system('cls')
    elif order in MENU:
        availability = check_resources(MENU[order])
        if availability == True:
            print(f"{order} costs ${MENU[order]["cost"]}")
            print("Please enter the coins.")
            valid_input = False
            while not valid_input:
                try:
                    quarter = int(input("How many Quarters? : "))* 0.25
                    dimes = int(input("How many Dimes? : "))* 0.10
                    nickles = int(input("How many Nickles? : "))* 0.05
                    pennies = int(input("How many Pennies? : "))* 0.01
                    total_amount = quarter + dimes + nickles + pennies
                    valid_input = True
                except:
                    print("Please enter coins correctly")
                
            success, message = check_payment(MENU[order], total_amount)
            if success:
                coffee_machine(MENU[order])
                print(message)
                print(f"Here is your {order}")
                money += MENU[order]["cost"]
            else:
                print("Transaction cancelled")
            input("Press ENTER to continue.....")
            os.system('cls')
            # print(f'Report\nWater: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}')
    elif order == "off":
        machine_is_on = False
    elif order == "refill":
        refill()
    else:
        print("Invalid input. Please choose from espresso/latte/cappuccino.")
        input("Press ENTER to continue...")

    
