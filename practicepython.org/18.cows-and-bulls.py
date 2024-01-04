"""
Create a program that will play the “cows and bulls” game with the user. 
The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 

- For every digit that the user guessed correctly in the correct place, 
they have a “cow”. 
- For every digit the user guessed correctly in the wrong place is a “bull.” 

Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. 

Keep track of the number of guesses the user makes throughout the game and 
tell the user at the end.
"""

import random

def return_num(): 
    n = random.randint(1000, 9999)
    return [i for i in str(n)]


values = return_num()

print(values)


def game_mode():
    game_on = True
    count = 0
    
    while game_on:
        num = input("Guess a 4 digit number: ")
        bull, cow = 0, 0
        count += 1

        if ''.join(values) == num:
            game_on = False

        else:

            for i in range(len(num)):
                if num[i] == values[i]:
                    bull += 1
                elif num[i] in values:
                    cow += 1
            print(f"{bull}bulls, {cow} cows")

    return f"You guessed the number in {count} {'attempt' if count == 1 else 'attempts'}."



res = game_mode()
print(res)
        
        
    
