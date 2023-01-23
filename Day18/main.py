# https://docs.python.org/3/library/turtle.html
import random
import turtle as t


tim = t.Turtle()
t.colormode(255)

# Generate a random RGB color - Python Tuples
# Tuples, unlike list, once assigned cannot be changed
# my_tuple(1, 2, 3)
# my_tuple[0] is equal to 1
# you can convert a tuple to a list using my_list = list(my_tuple)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_color = (r, g, b)
    return ran_color

#Spirograph
def draw_spirograph(size_of_gap):
   for heading in range(int(360 / size_of_gap)):
     tim.color(random_color())
     tim.circle(100)
     tim.setheading(tim.heading() + size_of_gap)

tim.shape("turtle")
#tim.color("purple")

# Draw a square
#for _ in range(4):
#   tim.forward(100)
#   tim.right(90)

#Draw a dashed line
#for _ in range(15):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()

#Draw 3-sided to 10 sided shapes and colors
#colors = ["red", "green", "purple", "orange", "blue", "yellow", "brown", "black", "pink", "midnight blue"]
#for shape in range(3, 11):
#    angle = 360 / shape
#    tim.color(random.choice(colors))
#    for _ in range(shape):
#        tim.forward(100)
#        tim.right(angle)

# Random Walk - same distance random direction, random color
#direction = [0, 90, 180, 270]
#tim.pensize(10)
#tim.speed("fast")

#for _ in range(50):
#  tim.color(random_color())
#  tim.forward(50)
#  tim.setheading(random.choice(direction))


tim.speed("fastest")
tim.hideturtle()

#Spirograph
draw_spirograph(2)


screen = t.Screen()
screen.exitonclick()