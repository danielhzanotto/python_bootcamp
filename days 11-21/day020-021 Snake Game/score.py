from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center",
                   font=("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=(
            "Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
