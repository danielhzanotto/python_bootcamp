from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score_1 = 0
        self.score_2 = 0
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"{self.score_1}    {self.score_2}", align="center",
                   font=("Courier", 15, "normal"))

    def win_game(self):
        self.goto(0, 0)
        self.write(f"YOU WIN", align="center", font=(
            "Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=(
            "Courier", 24, "normal"))

    def increase_player_score(self):
        self.score_1 += 1
        self.clear()
        self.update_scoreboard()

    def increase_pc_score(self):
        self.score_2 += 1
        self.clear()
        self.update_scoreboard()
