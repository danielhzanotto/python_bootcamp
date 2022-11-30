from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.screensize(600, 600)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Score()

is_on = True
while is_on:
    screen.update()
    time.sleep(.1)

    snake.move()
    if snake.head.distance(food.food) < 10:
        food.place_food()
        snake.grow()
        scoreboard.increase_score()

    if (snake.head.xcor() >= screen.canvwidth / 2) or (snake.head.xcor() <= - screen.canvwidth / 2) or (snake.head.ycor() >= screen.canvheight / 2) or (snake.head.ycor() <= -screen.canvheight / 2):
        is_on = False
        scoreboard.game_over()

    for pixel in range(2, len(snake.snake) - 1):
        if snake.snake[pixel].pos() == snake.head.pos():
            is_on = False
            scoreboard.game_over()


screen.exitonclick()
