from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def reset_turtle():
    tim.reset()

screen.listen()

screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="w", fun=move_forwards)

screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="s", fun=move_backwards)

screen.onkey(key="A", fun=turn_left)
screen.onkey(key="a", fun=turn_left)

screen.onkey(key="D", fun=turn_right)
screen.onkey(key="d", fun=turn_right)

screen.onkey(key="C", fun=reset_turtle)
screen.onkey(key="c", fun=reset_turtle)

screen.exitonclick()
