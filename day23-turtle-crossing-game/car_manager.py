from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, current_level):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250, 260))
        self.setheading(180)
        self.move_speed = STARTING_MOVE_DISTANCE + ((current_level - 1) * MOVE_INCREMENT)
        self.move_increment = MOVE_INCREMENT
        self.move()

    def move(self):
        self.forward(self.move_speed)
