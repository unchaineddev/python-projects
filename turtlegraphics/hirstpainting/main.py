
#### To extract color list ###

#import colorgram
#
#colors = colorgram.extract("image.jpg",30)
#print(colors)
#
#rgbcolors = []
#
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_colors = (r,g,b)
#    rgbcolors.append(new_colors)
#
#print(rgbcolors)

from turtle import Turtle, Screen
import turtle as t
import random

turt = t.Turtle()
t.colormode(255)
t.speed("fastest")
t.penup()
t.hideturtle()

listcolors = [(210, 67, 183), (128, 70, 207), (157, 81, 38), (122, 150, 67), (59, 82, 149), (127, 206, 165),
(178, 190, 214), (63, 21, 69), (166, 62, 154), (76, 135, 94), (211, 167, 126), (20, 54, 180)]

t.setheading(225)
t.forward(300)
t.setheading(0)
no_dots = 101


for count in range(1, no_dots):
    t.dot(20, random.choice(listcolors))
    t.forward(50)

    if count % 10 ==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = Screen()
screen.exitonclick()

