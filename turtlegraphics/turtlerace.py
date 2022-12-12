from turtle import Turtle, Screen
import random


screen = Screen()


race_on = True
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will the race?")
colors = ["red","blue", "green", "yellow", "pink"]
allturt = []

y_positions = [ -70, -40, -10, 20, 50]



for turtle_index in range(0,5):
    t = Turtle (shape="turtle")
    t.penup()
    t.color(colors[turtle_index])
    t.goto(x=-230, y=y_positions[turtle_index])
    allturt.append(t)

if user_bet:
    race_on: True
    
while race_on:

    for turtle in allturt:
        if turtle.xcor() > 230:
            # exits once its complete
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"The {winning_color} color has won, Congrats !!")
            else:
                print(f"The {winning_color} has lost, Oops !!")
                
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)


screen.exitonclick()

