from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    """Class responsible for keeping the score and printing it"""
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-275, 260)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """refresh the screen writing"""
        self.clear()
        self.write(f"level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """print the game over text"""
        self.goto(-80, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)
