from turtle import Screen
from crosser import Crosser
import time
from car import Car
from score import Score

screen = Screen()
screen.screensize(1000, 600)
screen.setup(width=1000, height=600)
screen.tracer(0)

scoreboard = Score()
tim = Crosser()
cars = Car()

counter = 0

is_on = True
while is_on:
    if scoreboard.key == counter:
        car = cars.generate_cars()
        counter = 0

    tim.move()
    cars.move_car()

    cars.car_hit(tim, scoreboard)

    scoreboard.set_score(tim)

    counter += 1
    time.sleep(0.1)
    screen.update()

    if scoreboard.finish:
        is_on = False


screen.exitonclick()
