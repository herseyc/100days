import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.onkey(fun=player.move_turtle_up, key="Up")
screen.onkey(fun=player.move_turtle_right, key="Right")
screen.onkey(fun=player.move_turtle_left, key="Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect successful crossing
    if player.is_at_finishline():
        player.goto_start()
        car_manager.level_up()
        score_board.increase_level()



screen.exitonclick()