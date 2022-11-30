from turtle import Turtle, Screen
screen = Screen()


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.setx(position)
        self.direction = "up"

    def up(self):
        if self.ycor() < 270:
            self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() > -270:
            self.sety(self.ycor() - 20)

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
        if self.ycor() >= 270:
            self.direction = "down"
        elif self.ycor() <= -270:
            self.direction = "up"
