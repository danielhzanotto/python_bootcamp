from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(.5, .5)
        self.color("white")
        self.direction = [0, 1]
        self.velocity = 0.1

    def north(self):
        if self.ycor() < 280:
            self.sety(self.ycor() + 10)

    def south(self):
        if self.ycor() > -280:
            self.sety(self.ycor() - 10)

    def east(self):
        if self.xcor() < 490:
            self.setx(self.xcor() + 10)

    def west(self):
        if self.xcor() > -490:
            self.setx(self.xcor() - 10)

    def set_direction(self, player_1, player_2):
        if self.ycor() == 280 or self.ycor() == -280:
            self.bounce_y(self.direction)

        if player_1.distance(self) <= 30 and self.xcor() <= -460 or player_2.distance(self) <= 30 and self.xcor() >= 460:
            self.bounce_x(self.direction)

        if self.xcor() == 490 or self.xcor() == -490:
            self.direction[0] = 2
            self.direction[1] = 2

    def ball_move(self):
        if self.direction[0] == 0:
            self.north()
        elif self.direction[0] == 1:
            self.south()
        if self.direction[1] == 0:
            self.east()
        elif self.direction[1] == 1:
            self.west()

    def bounce_y(self, direction):
        if direction[0] == 0:
            direction[0] = 1
        else:
            direction[0] = 0
        self.velocity *= 0.8

    def bounce_x(self, direction):
        if direction[1] == 0:
            direction[1] = 1
        else:
            direction[1] = 0
        self.velocity *= 0.9
