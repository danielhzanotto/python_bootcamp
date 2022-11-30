from turtle import Turtle, Screen
import random
import colorgram

rgb_colors = []
colors = colorgram.extract('spot-painting.jpg', 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

tim = Turtle()
tim.shape("turtle")

screen = Screen()
screen.colormode(255)

range_a = int(screen.screensize()[0] / 20)
range_b = int(screen.screensize()[1] / 20)

pos_h = int(- screen.screensize()[0] / 2)
pos_v = int(- screen.screensize()[1] / 2)

tim.up()
tim.setpos(pos_h, pos_v)

for h in range(range_b):

    for v in range(range_a):
        tim.down()
        tim.color(rgb_colors[random.randint(1, len(rgb_colors) - 1)])
        tim.dot(10)
        tim.up()
        tim.forward(range_a)

    pos_v += range_b
    tim.setpos(pos_h, pos_v)


screen.exitonclick()
