from turtle import Screen
import time 
from action import Snake 
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("You are a snake")

# screen tracer to stop animation
screen.tracer(0)

sn = Snake()
food = Food()
score = ScoreBoard()

screen.listen()

screen.onkey(sn.up, "Up")
screen.onkey(sn.down, "Down")
screen.onkey(sn.left, "Left")
screen.onkey(sn.right, "Right")

# Moving the snake 
game_on = True
while game_on:
    # To update screen
    screen.update()
    time.sleep(0.1)
    sn.move()

    # Collision from food
    if sn.head.distance(food) < 15:
        food.refresh()
        sn.size_increase()
        score.increase_score()

    if sn.head.xcor() >290 or sn.head.xcor() < -290 or sn.head.ycor()>290 or sn.head.ycor()<-290:
        game_on = False
        score.game_over()


    # Collision with tail 

    for segment in sn.body[1:]:
        if sn.head.distance(segment) < 10:
                    game_on = False
                    score.game_over()
    
screen.exitonclick()

