import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtle_list = []

is_race_on = False


def return_name(index_turtle):
    return "timmy" + index_turtle


for index in range(6):
    name_turtle = return_name(str(index))
    name_turtle = Turtle("turtle")
    turtle_list.append(name_turtle)
    name_turtle.color(colors[index])
    name_turtle.penup()
    name_turtle.goto(x=-240, y=-100 + index * 50)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
