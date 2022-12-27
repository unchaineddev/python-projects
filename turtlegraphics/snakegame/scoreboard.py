from turtle import Turtle
ALIGN = "center"
FONT = ("Courier",18, "normal")
FONTOVER = ("Monospace", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        #self.highscore = 0
        with open("highscores.txt") as hs:
            self.highscore = int(hs.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.highscore}",align=ALIGN,font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscores.txt",mode="w") as hs:
                hs.write(f"{self.highscore}")
        self.score = 0
        self.update_score()


#    def game_over(self):
#        self.goto(0,0)
#        self.write("GAME OVER", align=ALIGN, font=FONTOVER)
