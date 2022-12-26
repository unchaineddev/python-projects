COLORS = ["red", "blue", "green", "yellow", "pink", "purple"]
STARTING_MOVE_DIST = 5
MOVE_INCREMENT = 10


from turtle import Turtle
import random


# Creating  a Car Manager Class
class CarManager(Turtle):
    def __init__(self):
        self.allcars = []
        self.carspeed = STARTING_MOVE_DIST


# Creating a car 
    def create_car(self):
        random_chance = random.randint(1,7)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.allcars.append(new_car)


# Moving a car 
    def move_cars(self):
        for car in self.allcars:
            car.backward(self.carspeed)


# Increase speed
    def levelup(self):
        self.carspeed += MOVE_INCREMENT

