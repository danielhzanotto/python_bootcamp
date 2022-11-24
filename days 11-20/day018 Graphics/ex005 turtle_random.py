from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")
tim.pensize(3)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


screen = Screen()
screen.colormode(255)

for round in range(30):
    tim.pencolor(random_color())

    tim.seth(random.choice([0, 90, 180, 270]))
    tim.forward(30)


screen.exitonclick()
