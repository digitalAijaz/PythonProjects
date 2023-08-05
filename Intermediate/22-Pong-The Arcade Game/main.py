from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.title("Pong Game by Aijaz")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350,0), "red")
l_paddle = Paddle((-350,0), "blue")

ball = Ball("yellow")
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with top & bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        #ball.ball_speed *= 1.1

    # Detect when Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.update_l_scoreboard()
        ball.move_speed = 0.1

    # Detect when Left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.update_r_scoreboard()
        ball.move_speed = 0.1

screen.exitonclick()