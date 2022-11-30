from turtle import Turtle
import time


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = [0, 0]
        self.update_scoreboard()
        self.hideturtle()
        self.winner = ""

    def update_scoreboard(self):
        self.write(f"{self.score[0]}    {self.score[1]}", align="center",
                   font=("Courier", 15, "bold"))

    def win_game(self):
        self.goto(0, 0)
        if self.score[0] > self.score[1]:
            self.winner = "PLAYER 1"
        elif self.score[1] > self.score[0]:
            self.winner = "PLAYER 2"
        self.write(f"{self.winner} WINS", align="center", font=(
            "Courier", 24, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=(
            "Courier", 24, "normal"))

    def set_score(self, ball):
        if ball.xcor() >= 490:
            self.score[0] += 1
            ball.goto(0, 0)
            ball.velocity = 0.1
            time.sleep(1)
        if ball.xcor() <= -490:
            self.score[1] += 1
            ball.goto(0, 0)
            ball.velocity = 0.1
            time.sleep(.7)
        self.clear()
        self.update_scoreboard()
        if self.score[0] == 5 or self.score[1] == 5:
            self.win_game()
            ball.velocity = 0.1
