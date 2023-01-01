from turtle import Turtle, Screen
import pandas as pd


us = Turtle()


screen = Screen()
screen.title("Guess the United States")


# Load Image from file
image = "blank_states_img.gif"
screen.addshape(image)
us.shape(image)


data = pd.read_csv("./50_states.csv")
allstates = data.state.to_list()
guessed_state = []

while len(guessed_state) <50:
    # Prompt to ask user input
    answer = screen.textinput(title=f"{len(guessed_state)} out of 50 States",prompt="Guess a State? ").title()

    if answer == "Exit":
        missing_states = [state for state in allstates if state not in guessed_state]
#       missing_states = []
#       for state in allstates:
#            if state not in guessed_state:
#                missing_states.append(state)
        new_data= pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # If answer in one of the states in the csv file
    if answer in allstates:
        guessed_state.append(answer)
        us.hideturtle()
        us.penup()
        state_data = data[data.state == answer]
        us.goto(int(state_data.x),int(state_data.y))
        us.write(answer)



screen.exitonclick()



# To find the location co-ordinates of the state
#def co_ordinate(x, y):
#    print(x, y)
#
#screen.onscreenclick(co_ordinate)
#
#screen.mainloop()


