from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
is_on = True


def is_off():
    is_on = False
    return is_on


while is_on:
    snake.move()
    screen.onkey(key="q", fun=is_off)
    screen.update()
    time.sleep(.15)

screen.exitonclick()
