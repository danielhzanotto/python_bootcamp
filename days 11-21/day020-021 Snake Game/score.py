from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        with open("days 11-21/day020-021 Snake Game/score.txt") as data:
            self.highest = int(data.read())
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}          Highest Score: {self.highest}", align="center",
                   font=("Courier", 15, "normal"))

    def reset(self):
        if self.score > self.highest:
            with open("days 11-21/day020-021 Snake Game/score.txt", mode="w") as data:
                self.highest = self.score
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
