import turtle as t
import random

tim = t.Turtle()
tim.hideturtle()
t.colormode(255)

x_coord = tim.xcor() - 200
y_coord = tim.ycor() - 200
tim.penup()
tim.goto(x_coord, y_coord)
tim.pendown()

color_list = \
    [
        (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
        (170, 154, 41),
        (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
        (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
        (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
    ]

def random_color():
    return random.choice(color_list)


def move_forward(distance):
    tim.penup()
    tim.forward(distance)
    tim.pendown()

def draw_hirst_painting(columns, rows):
    new_y = 0
    for y in range(rows):
        for x in range(columns):
            tim.color(random_color())
            tim.dot(20)
            move_forward(50)
        tim.penup()
        new_y = y_coord + 50 * (y+1)
        tim.goto(x_coord, new_y)
        tim.pendown()


draw_hirst_painting(10, 10)

screen = t.Screen()
screen.exitonclick()
