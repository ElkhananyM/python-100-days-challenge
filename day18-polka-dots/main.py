# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)

# ---------------------------------------------------------------------------------------------------------------
# import turtle as turtle_module
# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
# screen = turtle_module.Screen()
# screen.exitonclick()
# ---------------------------------------------------------------------------------------------------------------





# 10x10 polka dots, 20 pixels per dot, spaced apart by 50 pixels

import turtle as t
import random

screen = t.Screen()
t.colormode(255)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
tim.speed(0)
screen_width = screen.window_width()
screen_height = screen.window_height()
southwest_x = (-screen_width // 2) + 50
southwest_y = (-screen_height // 2) + 50
tim.penup()
tim.goto(southwest_x, southwest_y)
tim.pendown()

def move_tim():
    tim.penup()
    tim.forward(50)
    tim.pendown()

def draw_polka():
    tim.color(random.choice(color_list))
    tim.begin_fill()
    tim.circle(20)
    tim.end_fill()
    move_tim()

for i in range(1, 11):
    for _ in range(10):
        draw_polka()
    tim.penup()
    southwest_y += 50
    tim.goto(southwest_x, southwest_y)
    tim.pendown()


screen.exitonclick()