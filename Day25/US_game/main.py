import turtle 
import pandas as pd


screen = turtle.Screen()
screen.title("US states guessing game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
states = data['state'].tolist()
guessed_states = []
missing_states = []
while len(guessed_states) < len(states):
    answer_state = screen.textinput(title="Guess the State", prompt=f"{len(guessed_states)}/50 What's another states name").title()
    # d = data[data['state'] == 'Florida']
    # print(d['x'])
    if answer_state == "Exit":
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_csv = pd.DataFrame(missing_states)
        new_csv.to_csv("learn_states")
        break
    if answer_state in states:
        d = data[data['state'] == answer_state]
        guessed_states.append(answer_state)
        new_x = d['x'].item()
        new_y = d['y'].item()
        peter = turtle.Turtle("circle")
        peter.penup()
        peter.hideturtle()
        peter.goto(new_x, new_y)
        peter.write(f"{answer_state}", align="center", font=("Arial", 8, "normal"))

missing_states