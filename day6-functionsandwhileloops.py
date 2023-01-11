
# Python Built-in Functions
# https://docs.python.org/3/library/functions.html

# print() and len() are built in functions
print("Hello")
num_char = len("Hello")
print(num_char)

# Simple Function
# Define the function
def my_function():
  #What the function does
  print("Hello")
  print("Bye")

#Calling the function
my_function()

#While Loops
#while something_is_true:
#    Do things

count = 5
while count > 0:
  print(count)
  count -= 1


count = 0
check = False
while not check:
  if count == 4:
    check = True
  print(check)
  count += 1

#Reeborg's World https://reeborg.ca/reeborg.html
