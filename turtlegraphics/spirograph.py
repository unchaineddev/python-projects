import turtle as t 
import random


turt = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color


turt.speed("fastest")

def draw_spirograph(sizeofgap):
    for _ in range(int(360/sizeofgap)):
        turt.color(random_color())
        turt.circle(100)
        turt.setheading(turt.heading()+ sizeofgap)

draw_spirograph(15)

screen = t.Screen()
screen.exitonclick()

