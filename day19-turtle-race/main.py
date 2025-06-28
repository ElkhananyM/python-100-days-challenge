import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_pos = -230
y_pos = -60
is_race_on = False
all_turtles = []

def new_turtle(color, x_coords, y_coords):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color)
    tim.goto(x=x_coords, y=y_coords)
    all_turtles.append(tim)

for color in colors:
    new_turtle(color, x_pos, y_pos)
    y_pos += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()