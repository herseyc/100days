
import turtle as turtle_module
import random

# Requirements
# 10 lines of 10 dots ( 10 rows, 10 columns) = 100 dots
# Dot size 20
# each dot is a random color from the generated pallet (color list)
# 50 steps between dots
# 50 steps between lines of dots

tim = turtle_module.Turtle()
turtle_module.colormode(255)

# Generate Color List using colorgram
#import colorgram
#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

# Generated Color List using the code above and removing the "white" and near white.
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

number_of_dots = 100
tim.speed("fastest")
tim.penup()

# Set initial position of tim to the lower right
tim.setheading(225)
tim.forward(250)

# Reset the heading and hide tim
tim.setheading(0)
tim.hideturtle()

for dotcount in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    # after 10 dots go up and back to start of row
    if dotcount % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()