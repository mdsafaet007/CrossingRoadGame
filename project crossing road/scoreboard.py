from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.lvl}", align="left", font=FONT)

    def increase_score(self):
        self.lvl += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="Center", font=FONT)
