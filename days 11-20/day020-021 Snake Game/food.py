from turtle import Turtle
import random


class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.shape("square")
        self.food.color("coral")
        self.food.penup()
        self.place_food()

    def place_food(self):
        self.food.goto((float(random.randrange(-280, 280, 20))),
                       (float(random.randrange(-280, 280, 20))))
