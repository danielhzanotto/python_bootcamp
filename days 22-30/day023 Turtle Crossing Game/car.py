from turtle import Turtle
import random
import time

COLORS = ("blue", "orange", "green", "yellow", "red", "purple")
STARTING_MOVE_DISTANCE = 5


class Car():
    def __init__(self):
        self.all_cars = []

    def generate_cars(self):
        car = Turtle()
        car.penup()
        car.color(COLORS[random.randint(0, 5)])
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(460, random.randrange(-230, 250, 20))
        self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            if car.xcor() > -520:
                car.setx(car.xcor() - 20)

    def car_hit(self, turtle, score):
        for car in self.all_cars:
            if car.distance(turtle) <= 15 and turtle.ycor() == car.ycor():
                score.lives -= 1
                turtle.sety(-270)
                time.sleep(.7)
