FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)

    def updatescore(self):
        self.clear()
        self.color("white")
        self.write(f"level: {self.level}", align="left", font=FONT)


    def increaselevel(self):
        self.level += 1
        self.updatescore()


    def gameover(self):
        self.goto(0,0)
        self.color("white")
        self.write(f"GAME OVER", align="center", font=FONT)
