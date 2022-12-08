from turtle import Turtle, Screen

turt = Turtle()

for _ in range(15):
    turt.forward(10)
    turt.penup()
    turt.forward(10)
    turt.pendown()

screen = Screen()
screen.exitonclick()
