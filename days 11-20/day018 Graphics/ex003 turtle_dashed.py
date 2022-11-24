from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

for _ in range(15):
    tim.forward(10)
    tim.up()
    tim.forward(10)
    tim.down()

screen = Screen()
screen.exitonclick()
