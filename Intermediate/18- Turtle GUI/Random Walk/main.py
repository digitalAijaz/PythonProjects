import turtle as t
import random

tim = t.Turtle()

t.colormode(255)
tim.color("magenta")
tim.speed("fastest")
tim.pensize(5)

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]

for _ in range(500):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(directions))

screen = t.Screen()
t.exitonclick()