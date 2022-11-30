from turtle import Screen
from paddle import Paddle
import time
from score import Score
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.screensize(1000, 600)
screen.setup(width=1000, height=600)
screen.title("PONG")
screen.tracer(0)

scoreboard = Score()
ball = Ball()

player = Paddle(-470)
pc = Paddle(470)

is_on = True
while is_on:
    pc.control_player_2()
    player.control_player_1()
    ball.set_direction(player, pc)
    ball.ball_move()
    scoreboard.set_score(ball)

    if len(scoreboard.winner) != 0:
        is_on = False

    screen.update()
    time.sleep(ball.velocity)

screen.exitonclick()
