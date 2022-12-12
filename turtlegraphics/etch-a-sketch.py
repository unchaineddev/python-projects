from turtle import Turtle, Screen


turt = Turtle()
screen = Screen()

def move_forw():
    turt.forward(20)

def move_back():
    turt.backward(20)

def move_left():
    turt.lt(10)

def move_right():
    turt.rt(10)

def clr():
    turt.penup()
    turt.clear()
    turt.home()
    turt.down()


screen.listen()
screen.onkey(move_forw,"w")
screen.onkey(move_back,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(clr,"c")


screen.exitonclick()
