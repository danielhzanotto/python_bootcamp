from turtle import Turtle, Screen

screen = Screen()

POSITION = [(0, -20), (0, 0), (0, 20)]


class Paddle():
    def __init__(self):
        self.paddle = []
        self.direction = "up"

    def create_paddle(self):
        for r in range(0, 3):
            piece = Turtle()
            piece.color("white")
            piece.penup()
            piece.shape("square")
            piece.goto(POSITION[r])
            self.paddle.append(piece)

    def create_player(self):
        self.create_paddle()
        for piece in self.paddle:
            piece.setx(-570)

    def create_pc(self):
        self.create_paddle()
        for piece in self.paddle:
            piece.setx(570)

    def up(self):
        if self.paddle[2].ycor() < 280:
            for piece in self.paddle:
                piece.sety(piece.ycor() + 20)

    def down(self):
        if self.paddle[0].ycor() > -280:
            for piece in self.paddle:
                piece.sety(piece.ycor() - 20)

    def control_player(self):
        screen.listen()
        screen.onkeypress(key="Up", fun=self.up)
        screen.onkeypress(key="Down", fun=self.down)

    def pc_move(self):
        self.directions()
        if self.direction == "up":
            return self.up()
        elif self.direction == "down":
            return self.down()

    def directions(self):
        if self.paddle[2].ycor() >= 280:
            self.direction = "down"
            return "down"
        elif self.paddle[0].ycor() <= -280:
            self.direction = "up"
            return "up"
        else:
            return self.direction
