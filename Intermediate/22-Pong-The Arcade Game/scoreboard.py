from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("orange")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def update_scores(self):
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 60, "normal"))

    def update_l_scoreboard(self):
        self.clear()
        self.l_score += 1
        self.update_scores()

    def update_r_scoreboard(self):
        self.clear()
        self.r_score += 1
        self.update_scores()