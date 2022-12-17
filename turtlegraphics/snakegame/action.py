from turtle import Turtle

POSITIONS  = [(0,0),(-20,0), (-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270 
LEFT = 180
RIGHT = 0

""" Class Snake """

class Snake:
    #Create a snake body 
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def add_segment(self,pos):
        s = Turtle("square")
        s.color("green")
        s.penup()
        s.goto(pos)
        self.body.append(s)


    # increases the size of the snake  
    def size_increase(self):
        self.add_segment(self.body[-1].pos())

    def move(self):
        for number in range(len(self.body)-1, 0, -1):
            x = self.body[number - 1].xcor()
            y = self.body[number - 1].ycor()
            self.body[number].goto(x, y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
           



