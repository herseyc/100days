from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Draw Game Board
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# Disable animation
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

# Paddles Moves - Screen listen
screen.listen()

# Move right paddle
screen.onkey(fun = r_paddle.go_up, key = "Up")
screen.onkey(fun = r_paddle.go_down, key = "Down")

# Move right paddle
screen.onkey(fun = l_paddle.go_up, key = "w")
screen.onkey(fun = l_paddle.go_down, key = "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    # Update screen
    screen.update()
    ball.move()

    #Detect Collision with Top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Bounce
        ball.bounce_y()

    # Detect Collision with Paddles
    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < - 320:
        ball.bounce_x()

    # Detect Miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()