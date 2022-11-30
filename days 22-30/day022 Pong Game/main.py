from turtle import Screen
from paddle import Paddle
import time
from score import Score
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.screensize(1200, 600)
screen.setup(width=1200, height=600)
screen.title("PONG")
screen.tracer(0)

scoreboard = Score()
ball = Ball()

player = Paddle()
player.create_player()

pc = Paddle()
pc.create_pc()


is_on = True
while is_on:
    pc.pc_move()
    player.control_player()

    screen.update()
    time.sleep(.1)

screen.exitonclick()
