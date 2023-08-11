from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("orange")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 10)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #     self.goto(0, -24)
    #     self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
