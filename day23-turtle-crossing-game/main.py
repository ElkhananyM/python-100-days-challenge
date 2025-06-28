import time
from turtle import Screen
from player import Player
import random
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
cars = []
current_level = 1

screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # Generates a car every 6 frames, going down by 1 with each level to keep up with spawn vs speed of cars.
    if random.randint(1, 7 - current_level) == 1:
        new_car = CarManager(current_level)
        cars.append(new_car)

    # Score and level update
    if player.ycor() > player.finish_line:
        scoreboard.next_level()
        player.next_level()
        for car in cars:
            car.move_speed += car.move_increment
        current_level += 1

    # Loops through all cars and moves them
    for car in cars:
        car.move()
        if car.xcor() < -300:
            cars.remove(car)
            car.hideturtle()

    # Collision detection with cars
    for car in cars:
        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False

    screen.update()
screen.exitonclick()
