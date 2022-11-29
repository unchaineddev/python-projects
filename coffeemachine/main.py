from logo import logo

MENU = {
        "espresso": {
            "ingredients": {
                "water":  50,
                "coffee": 18,
                },
            "cost": 120,
            },
        "latte": {
            "ingredients": {
                "water" : 200,
                "coffee": 24,
                "milk"  : 150,
                },
                "cost": 140,
            },
        "cappuccino": {
            "ingredients": {
                "water" : 250,
                "coffee": 24,
                "milk"  : 100,
                },
                "cost": 150,
            }
        }

paisa = 0
resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        }


def resources_left(order):
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry, There are not enough {item} rn.")
            return False
    return True

def transact():
    print("Please enter 10/20/50/100 Rupee Notes to buy some coffee")
    #Prices - 120,140,150 
    total = int(input("How many 10 Rupee Notes: ")) * 10
    total += int(input("How many 20 Rupee Notes: ")) * 20
    total += int(input("How many 50 Rupee Notes: ")) * 50
    total += int(input("How many 100 Rupee Notes: ")) * 100
    return total 


def transaction_success(receivedmoney,drinkcost):
    if receivedmoney >= drinkcost:
        change = round(receivedmoney - drinkcost,2)
        print(f"Here is your change i.e Rs {change}")
        global paisa
        paisa += drinkcost
        return True
    else:
        print("Sorry that's not enough money. Money is refunded back to you")
        return False


def make_coffee(drink_name, order):
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your {drink_name}, ☕Enjoy your coffee!! ☕")


machine_on  = True 

while machine_on:
    print(logo)
    choice = input("What would you like? | Espresso | latte | cappuccino | ")
    if choice == "off":
        machine_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs {paisa}")
    else:
        drink = MENU[choice]
        if resources_left(drink["ingredients"]):
            payment = transact()
            if transaction_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



