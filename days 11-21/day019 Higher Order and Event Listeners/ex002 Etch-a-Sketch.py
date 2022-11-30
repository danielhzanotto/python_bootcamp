from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def fowards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def rights():
    tim.right(10)


def lefts():
    tim.left(10)


def clear():
    screen.resetscreen()
    # tim.clear()
    # tim.penup()
    # tim.home()
    # tim.pendown()


screen.listen()
screen.onkeypress(key="w", fun=fowards)
screen.onkeypress(key="s", fun=backwards)
screen.onkeypress(key="d", fun=rights)
screen.onkeypress(key="a", fun=lefts)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
