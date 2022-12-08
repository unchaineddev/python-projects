from turtle import Turtle, Screen

turt = Turtle()


# changes shape and resizes it
turt.shape("turtle")
turt.color("olivedrab")


for _ in range(4):
    turt.forward(100)
    turt.right(90)


screen = Screen()
screen.exitonclick()
