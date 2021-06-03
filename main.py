import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# creating the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# creating the main objects to use throughout the program
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
car_manager.create_car()

# listen to the up button to move the player
screen.listen()
screen.onkey(player.go_up, "Up")

# variables to be used in the loop
loop_index = 0
density = 5  # to skip loop_index 5 times, to control the density
game_is_on = True

# Creating some initial cars
while len(car_manager.cars) < 25:

    # create cars and controls density, large number = less dense
    if loop_index == density:
        car_manager.create_car()
        loop_index = 0

    # move cars and deletes the exiting cars
    car_manager.move_cars()
    loop_index += 1

# Main loop of the game
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create cars and controls density, large number = less dense
    if loop_index == density:
        car_manager.create_car()
        loop_index = 0

    # move cars and deletes the exiting cars
    car_manager.move_cars()

    # Detect collision with the finish line
    if player.is_finish():
        player.goto_start()
        scoreboard.increase_level()
        car_manager.increase_cars_speed()

    # Detect collision with cars
    if car_manager.collision(player):
        scoreboard.game_over()
        game_is_on = False

    loop_index += 1

screen.exitonclick()
