from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fowards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_fowards) #this is a higher order function, because it's getting another function as an argument
screen.exitonclick()
