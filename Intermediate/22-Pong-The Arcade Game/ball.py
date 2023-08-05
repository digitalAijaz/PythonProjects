from turtle import Turtle


class Ball(Turtle):
    def __init__(self,color):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1.0, 1.0)
        self.color(color)
        self.ball_speed = 1
        self.move_speed = 0.1
        self.speed(self.ball_speed)

        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_coord = self.xcor() + self.x_move
        y_coord = self.ycor() + self.y_move
        self.goto(x_coord, y_coord)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.move_speed > 0.01:
            self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()









