from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """add a new car to the cars list"""
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        y_pos = random.randint(-250, 255)  # x ends between 320 and -320
        new_car.goto(300, y_pos)
        self.cars.append(new_car)

    def move_cars(self):
        """loops on all cars and moves them, also deletes exiting cars"""
        for car in self.cars:
            x_pos = car.xcor() - self.cars_speed
            car.goto(x_pos, car.ycor())
            if x_pos < -320:
                self.cars.remove(car)

    def increase_cars_speed(self):
        """increase the speed of the cars"""
        self.cars_speed += MOVE_INCREMENT

    def collision(self, player):
        """detects if the player hit a car"""
        for car in self.cars:
            if car.distance(player) < 25:
                return True
        return False
