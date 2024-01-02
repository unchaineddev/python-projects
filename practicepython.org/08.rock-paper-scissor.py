# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), 
# compare them, print out a message of 
# congratulations to the winner, and ask if 
# the players want to start a new game)

import random

game_name = "Welcome to Rock, Paper, Scissor Game"
print('~' * 70)
print(f"{game_name:*^70}")
print('~' * 70)

choices = ['r', 'p', 's']


def computer_choice():
    return random.choice(choices)



def user_choice(): 
    user_choice = input("Enter r for rock, p for paper, s for scissor: ").lower()
    if user_choice not in choices:
        print('Invalid input! try again')
    else:
        return user_choice
        


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!\n"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        return "You win!\n"
    else:
        return "Computer wins!\n"



def play_game():
    while True:
        computer = computer_choice()
        user = user_choice()

        print(f'User Choice: {user}')
        print(f'Computer Choice: {computer}')

        result = determine_winner(user, computer)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'y':
            print("\nThanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    play_game()

