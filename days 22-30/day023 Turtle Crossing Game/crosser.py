from turtle import Turtle, Screen
screen = Screen()


class Crosser(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.goto(0, -270)
        self.shapesize(0.5, 0.5)

    def go_up(self):
        if self.ycor() < 290:
            self.sety(self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -270:
            self.sety(self.ycor() - 20)

    def move(self):
        screen.listen()
        screen.onkeypress(key="Up", fun=self.go_up)
        screen.onkeypress(key="Down", fun=self.go_down)
