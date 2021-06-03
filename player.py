from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        """moves the player up"""
        y_pos = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_pos)

    def is_finish(self):
        """check if finish line reached"""
        return self.ycor() >= FINISH_LINE_Y

    def goto_start(self):
        """resets the player's position"""
        self.goto(STARTING_POSITION)
