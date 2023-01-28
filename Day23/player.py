from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto_start()


    def move_turtle_up(self):
        self.forward(MOVE_DISTANCE)

    def move_turtle_right(self):
        x_pos = self.xcor()
        self.goto(x_pos + MOVE_DISTANCE, self.ycor())

    def move_turtle_left(self):
        x_pos = self.xcor()
        self.goto(x_pos - MOVE_DISTANCE, self.ycor())

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finishline(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False