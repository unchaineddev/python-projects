import random
from logo import logo 
print(logo)

easy = 10 
difficult = 5


def game():
    """ Returns turns remaining"""
    def check(guess,number,turns):
        if guess>number:
            print("Too High")
            return turns - 1
        elif guess<number:
            print("Too less")
            return turns - 1
        else: 
            print(f"You got it! The answer is {number}")


    def difficulty(): 
        level = input("Choose the difficulty level: e for Easy or d for Difficult: ")
        if level == 'e':
            return easy
        else:
            return difficult


    print("Welcome to the Number Guessing Game! ")
    print("I am thinking of a number between 1 and 100\n")
    number = random.randint(1,100)
    turns = difficulty()
   
    guess = 0
    while guess != number:
        print(f"You have {turns} attempts to guess the number")
        guess = int(input("Enter your guess: ")) 
        turns = check(guess,number,turns)
        if turns == 0:
            print("You run out of guesses, you lose!")
            return
game()



