import random
import os
from logo import logo 

def deal_card():
    """returns random card"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(cards)
    return card 


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # if 11 in cards and 10 in cards and len(cards)==2:
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards) 

    
def compare (user_score, pc_score):
    if user_score == pc_score:
        return "Draw!"
    elif pc_score == 0:
        return "You lose! The opponent has Blackjack!"
    elif user_score == 0:
        return "You win! You have a Blackjack!"
    elif user_score > 21:
        return "You went over 21; You lose!!"
    elif pc_score > 21:
        return "Opponent went over 21, You win!!"
    elif user_score > pc_score:
        return "You win!!!"
    else:
        return "You Lose!!!"

# Empty lists
def play_game():
    print(logo)
    
    user_cards = []
    pc_cards = []
    gameover = False

# PC and User are given 2 cards each 
    for _ in range(2):
        user_cards.append(deal_card())
        pc_cards.append(deal_card())

# calling function calculate_score() to assign score for user and computer
    while not gameover:
        user_score = calculate_score(user_cards)
        pc_score = calculate_score(pc_cards)
        print(f"Your cards {user_cards}, and your score {user_score}")
        print(f"Computer's cards {pc_cards}")

        if user_score == 0  or pc_score == 0 or user_score > 21:
            gameover = True
        else:
            another_card = input("Type y to get another card or n to pass:")
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                gameover = True

        while pc_score < 17  and pc_score != 0:
            pc_cards.append(deal_card())
            pc_score = calculate_score(pc_score)

        print(f"Your final hand {user_cards}, score is {user_score}")
        print(f"Opponent hand {pc_cards}, score is {pc_score}")
        print(compare(user_score, pc_score))

while(input("Do you want to play a Blackjack Game? \n Type Y for Yes and N to exit: "))== 'y':
    os.system('clear')
    play_game()



