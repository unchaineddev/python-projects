from logos import logo
from data import data 
import random 
import os

def account():
    return random.choice(data)

def format(account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, is {desc}, from {country}"

def check(guess, accounta, accountb):
    if accounta > accountb:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    
    continuegame = True
    accounta = account()
    accountb = account()

    while continuegame:
        accounta = account()
        accountb = account()

        print(f"Compare A: {format(accounta)}")
        print(f"Compare B: {format(accountb)}")

        guess = input("Who has more followers?\n Type A or B: ").lower()
        a_followers = accounta["follower_count"]
        b_followers = accountb["follower_count"]

        highest = check(guess, a_followers, b_followers)

        os.system("clear")

        print(vs)
        if highest:
            score = score + 1
            print(f"You are correct, your current score is {score}")
        else: 
            print(f"Sorry that's wrong. Final score is: {score}")
            continuegame = False
game()


