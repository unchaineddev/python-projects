# Hangman Game by Yusuf 

import os
import random 
from art import *
from words import * 

chosen_word = random.choice(word_list)


print(logo)


# to display "_" instead of the no of letters
display = [ ]
word_length = len(chosen_word)

# lives 

lives = 6 

for letter in range(word_length):
    display += "_"

print(display)

the_end = False

while not the_end:
    guess = input("Guess a Letter:\n").lower()
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')



    if guess in display:
        print(f"You have already guessed {guess}")

   
    for pos in range((word_length)):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter 
    

    if guess not in chosen_word:
        print(f"You have guessed {guess} and it's not in the word.\n You lose a life :( \n")
        lives -= 1
        if lives == 0:
            the_end = True
            print("You lose!")
            print(f"The Word you could not guess was {chosen_word}")
     
    print(f"{' '.join(display)}") 

# check if letter not in word, and reduce lives
 
    if "_" not in display:
        the_end = True
        print("You win!!")


    print(stages[lives])
