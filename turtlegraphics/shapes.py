from turtle import Turtle, Screen
import random


turt = Turtle()


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shapes(sides):
    angle = 360 / sides 
    for _ in range(sides):
        turt.forward(100)
        turt.right(angle)


for shape_draw in range(3,11):
    turt.color(random.choice(colors))
    draw_shapes(shape_draw)


screen = Screen()
screen.exitonclick()
