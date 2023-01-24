from turtle import Turtle, Screen
import random



screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

#Prompt user for their bet
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)

colors =["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_pos = -70
finish_line = 225

# Create 6 turtles and add each to all_turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos)
    y_pos += 30
    all_turtles.append(new_turtle)

# Race is on, once user has placed a bet
if user_bet:
    is_race_on = True

# Draw the start and finish line
flag = Turtle()
flag.penup()
flag.goto(x=-210, y=-100)
flag.pendown()
flag.left(90)
flag.forward(200)
flag.penup()
flag.goto(x=230, y=-100)
flag.pendown()
flag.forward(200)
flag.hideturtle()

while is_race_on:

   for turtle in all_turtles:
       # Let's move
       rand_distance = random.randint(0, 10)
       turtle.forward(rand_distance)

       # Did we win?
       if turtle.xcor() > finish_line:
           # Race is over, we have a winner!
           is_race_on = False
           # Get the color of the winning turtle
           winning_turtle = turtle.pencolor()
           # Check your bet
           if winning_turtle == user_bet:
               print (f"You Won! You bet {user_bet} and {winning_turtle} is the winning turtle!")
           else:
               print(f"You Lost! You bet {user_bet} but {winning_turtle} is the winning turtle!")



screen.exitonclick()