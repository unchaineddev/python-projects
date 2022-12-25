from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Atari/Pong")
screen.tracer(0) #makes starting paddle pos -> constant


#left and right paddle positions
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()

#movement of paddles
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")


# if game is on -> update screen
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
# For the ball to bounce back within the walls
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()


    # collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor() < -320 :
        ball.bounce_x()

    # when right paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    # when left paddle misses
    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()
