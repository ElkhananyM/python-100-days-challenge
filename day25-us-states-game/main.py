import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_guessed = 0
states = pd.read_csv("50_states.csv")
guessed_states = []
all_states = states["state"].to_list()

while states_guessed < 50:
    answer_state = screen.textinput(title=f"{states_guessed}/50 States Guessed",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        new_data = pd.DataFrame(sorted(set(all_states) - set(guessed_states)))
        print(new_data)
        break

    if answer_state in guessed_states:
        continue

    for state in states["state"]:
        if answer_state == state:
            coor = states[states["state"] == state]
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            new_turtle.goto(coor.x.item(), coor.y.iloc[0])
            new_turtle.write(answer_state)
            states_guessed += 1
            guessed_states.append(answer_state)


# turtle.mainloop()

# List comprehension of the missing_states list.
# missing_states = [state for state in all_states if state not in guessed_states]