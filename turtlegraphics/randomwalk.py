from turtle import Turtle, Screen
import random


turt = Turtle()


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


direction = [0,90,180,270]
turt.pensize(10)
turt.speed("fastest")

for _ in range(200):
    turt.color(random.choice(colors))
    turt.forward(20)
    turt.setheading(random.choice(direction))
    


screen = Screen()
screen.exitonclick()
