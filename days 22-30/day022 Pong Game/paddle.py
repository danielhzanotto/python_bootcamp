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

    def create_player_1(self):
        self.create_paddle()
        for piece in self.paddle:
            piece.setx(-470)

    def create_player_2(self):
        self.create_paddle()
        for piece in self.paddle:
            piece.setx(470)

    def up(self):
        if self.paddle[2].ycor() < 280:
            for piece in self.paddle:
                piece.sety(piece.ycor() + 20)

    def down(self):
        if self.paddle[0].ycor() > -280:
            for piece in self.paddle:
                piece.sety(piece.ycor() - 20)

    def control_player_1(self):
        screen.listen()
        screen.onkeypress(key="w", fun=self.up)
        screen.onkeypress(key="s", fun=self.down)

    def control_player_2(self):
        screen.listen()
        screen.onkeypress(key="Up", fun=self.up)
        screen.onkeypress(key="Down", fun=self.down)

    def pc_move(self):
        self.pc_directions()
        if self.direction == "up":
            return self.up()
        elif self.direction == "down":
            return self.down()

    def pc_directions(self):
        if self.paddle[2].ycor() >= 280:
            self.direction = "down"
        elif self.paddle[0].ycor() <= -280:
            self.direction = "up"
