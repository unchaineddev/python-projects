print('''
*******************************************************************************
|                   |                   |                  |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
|                `"=._o`"=._      _`"=._                   |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
|        |o`"=._` , "` `; .". ,  "-._"-._; ;               |
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

step1 = input('You are at a cross road, where do you want to go? \n Type "Left" or "right?" \n').lower()

if step1 == 'left':
    print('You have arrived at a lake. There is an island in the middle.')
    step2 = input("Type 'wait' to wait for the boat or type 'swim' to swim across the lake \n").lower()
    if step2 == 'wait':
        print("You arrived at the door unharmed. There is a house with three doors. One Red, One Blue, One black. \n")
        step3 = input("Which color do you choose? \n ").lower()
        if step3 == 'red':
            print("It's a room full of fire. Game Over.")
        elif step3 =='blue':
            print("You found the treasure! You win!")
        elif step3 == 'black':
            print("You enter a room full of beasts. GAME OVER")
        else:
            print("You chose a room that does not exist. GAME OVER!")
    else:
                   print("You were attacked by a GROUT \n GAME OVER.")    
                       
else:
    print("You fell into a hole. GAME OVER")
