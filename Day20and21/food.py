from turtle import Turtle
import random

LOWBORDER = -240
HIGHBORDER = 240

#Class Food that inherits from Turtle
class Food(Turtle):

    def __init__(self):
        # Init from Turtle
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(LOWBORDER, HIGHBORDER)
        random_y = random.randint(LOWBORDER, HIGHBORDER)
        self.goto(random_x, random_y)

