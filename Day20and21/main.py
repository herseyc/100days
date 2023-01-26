from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create the snake from my Snake Class
snake = Snake()
# Create good
food = Food()
scoreboard = ScoreBoard()

# Listen for key presses
screen.listen()
# Control the snake with the error keys
screen.onkey(fun = snake.up, key = "Up")
screen.onkey(fun = snake.down, key = "Down")
screen.onkey(fun = snake.left, key = "Left")
screen.onkey(fun = snake.right, key = "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    # Move the snake
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        # Grow Snake
        snake.extend()
        # Update scoreboard
        scoreboard.increase_score()

    # Detect a collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect a collision with tail
    #if head collides with any segment in tail, then game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # print("Game Over")
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
