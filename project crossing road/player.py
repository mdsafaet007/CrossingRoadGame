from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_position()
        self.setheading(90)

    def gp_up(self):
        self.forward(MOVE_DISTANCE)

    def start_position(self):
        self.goto(STARTING_POSITION)

    def reach_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False
