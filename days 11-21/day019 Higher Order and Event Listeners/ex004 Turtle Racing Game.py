from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput(
    title="Make your bet!", prompt="Which Turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

score = 50
pos_y = -125
for index in range(0, 6):

    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=pos_y + score * index)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! {winning_color} is the winner!")
            else:
                print(f"You lost... The winner is {winning_color}!")


screen.exitonclick()
