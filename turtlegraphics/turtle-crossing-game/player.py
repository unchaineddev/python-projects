STARTING_POSITIONS = (0,-250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

from turtle import Turtle



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.startagain()
        self.setheading(90)


    def go_up(self):
        self.forward(MOVE_DISTANCE)


    def startagain(self):
        self.goto(STARTING_POSITIONS)


# Once finished, it continues from original position
    def finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
