from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from score import Score
import time


#screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# creating objects from classes
player = Player()
car_manager = CarManager()
score = Score()

# key presses
screen.listen()
screen.onkey(player.go_up, "Up")


# creating car and behavior
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()


# detect collision between car and turtle 
    for car in car_manager.allcars:
        if car.distance(player) < 20:
            game_on = False
            score.gameover()

# Refer Player and CarManager Class  
    if player.finished():
        player.startagain()
        car_manager.levelup()
        score.increaselevel()

screen.exitonclick()
