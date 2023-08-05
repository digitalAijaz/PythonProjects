from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.pos = position
        self.new_color = color
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color(self.new_color)
        self.shapesize(20)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.penup()
        self.goto(self.pos)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
