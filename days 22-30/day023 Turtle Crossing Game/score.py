from turtle import Turtle
import time


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.lives = 3
        self.key = 5
        self.finish = False
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}          LIVES: {self.lives}",
                   align="center", font=("Courier", 15, "bold"))

    def set_score(self, turtle):
        if turtle.ycor() > 270:
            self.score += 1
            time.sleep(0.3)
            self.key -= 1
            turtle.sety(-270)
            if self.score == 5:
                self.win_game()
            elif self.lives == 0:
                self.game_over()
        else:
            self.update_scoreboard()

    def win_game(self):
        self.goto(0, 0)
        self.write(f"CONGRATULATIONS, YOU WON!", align="center", font=(
            "Courier", 24, "bold"))
        self.finish = True

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=(
            "Courier", 24, "normal"))
        self.finish = True
