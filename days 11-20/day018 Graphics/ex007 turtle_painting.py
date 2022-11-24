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


range_a = int(screen.screensize()[0] / 20)
range_b = int(screen.screensize()[1] / 20)

pos_h = int(- screen.screensize()[0] / 2)
pos_v = int(- screen.screensize()[1] / 2)

tim.up()
tim.setpos(pos_h, pos_v)

for h in range(range_b):

    for v in range(range_a):
        tim.down()
        tim.color(random_color())
        tim.dot(10)
        tim.up()
        tim.forward(range_a)

    pos_v += range_b
    tim.setpos(pos_h, pos_v)


screen.exitonclick()
