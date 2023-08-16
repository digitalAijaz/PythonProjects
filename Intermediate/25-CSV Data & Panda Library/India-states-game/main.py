import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "india_map.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("indian_states.csv")
states = data.state.to_list()

states_num = 28

while len(states) > 0:
    answer_state = screen.textinput(title=f"{states_num-len(states)}/{states_num} States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #change color of text to dark green
        t.color("dark green")
        #change thickness of pen to 2
        t.pensize(2)
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        states.remove(answer_state)

# states_to_learn.csv
states_to_learn = pandas.DataFrame(states)
states_to_learn.to_csv("states_to_learn.csv")
