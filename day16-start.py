
# Turtle https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen

#timmy = Turtle()
#print(timmy)
#timmy.shape("turtle")
# Colors https://cs111.wellesley.edu/reference/colors
#timmy.color("green")
#timmy.forward(100)

# Attributes
#my_screen = Screen()
#print(my_screen.canvheight)
# Method
#my_screen.exitonclick()
#https://pypi.org/project/prettytable/


from prettytable import PrettyTable

# Creating table object from the PrettyTable class
table = PrettyTable()
# Use the add_column method to add columns to table object
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Attribute to change table cells to be left aligned
table.align = "l"

# Print the table object
print(table)













