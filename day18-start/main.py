import turtle as t
import random

# t.colormode(255)
# tim = t.Turtle()
# tim.pensize(10)
# tim.speed(0)
#
# def walk_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
# def walk_direction():
#     directions = [0, 90, 180, 270]
#     tim.color(walk_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(25)
#
# while True:
#     walk_direction()

tim = t.Turtle()
t.colormode(255)
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color((random_color()))
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()