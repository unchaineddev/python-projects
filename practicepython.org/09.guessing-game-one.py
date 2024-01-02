# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they 
# guessed too low, too high, or exactly right.

import random 

guess_number = random.randint(1, 10)

wrong_number = True
while wrong_number:
    n = int(input("Guess the number: "))
    if n < guess_number:
        print("too low!\n")
    elif n > guess_number:
        print("too high!\n")
    else:
        if n == guess_number:
            wrong_number = False
            print("You have guessed the number! ")

        play_again = input('Do you want to play again?: ')
        wrong_number = True if play_again == 'y' else exit()
