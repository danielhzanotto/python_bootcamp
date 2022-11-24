from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")

screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spiro(rounds):
    for round in range(rounds):
        tim.pencolor(random_color())

        tim.right(360/rounds)
        tim.circle(100)


draw_spiro(30)


screen.exitonclick()
