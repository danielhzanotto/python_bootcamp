from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")

screen = Screen()
screen.colormode(255)

for round in range(3, 13):
    tim.pencolor(random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    for c in range(round):
        tim.forward(50)
        tim.right(360/round)


screen.exitonclick()
