import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
#increase speed
tim.speed("fastest")
tim.pensize(5)

# Move the turtle to the top of the screen
tim.penup()
tim.setposition(-100,300)
tim.pendown()

tim.color("SeaGreen")

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 20):
    draw_shapes(shape_side_n)
    tim.color(random_color())

screen = Screen()

screen.exitonclick()
