from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(.5, .5)
        self.color("white")
        self.direction = [0, 1]

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
        if self.ycor() == 280:
            self.direction[0] = 1
        elif self.ycor() == -280:
            self.direction[0] = 0

        for piece in player_1.paddle:
            if piece.distance(self) <= 10:
                self.direction[1] = 0
        for piece in player_2.paddle:
            if piece.distance(self) <= 10:
                self.direction[1] = 1

        if self.xcor() == 490:
            self.direction[0] = 2
            self.direction[1] = 2
        elif self.xcor() == -490:
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
