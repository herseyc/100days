
# function with default values
def my_function(a=1, b=2, c=3):
    print(f"{a} {b} {c}")

# Using default args
my_function()
# Changing default args
my_function(a=20)

#Many positional arguments
# *args is a tuple
def add(*args):
    sumofnums = 0
    print(args)
    print(f"Argument at position 0: {args[0]}")
    for n in args:
        #print(f"{sumofnums} + {n}")
        sumofnums += n
        #print(sumofnums)
    print(f"Total: {sumofnums}")

add(1, 2, 3, 4)

#Many keyword arguments
# **kwargs is a dict
def calculate(n, **kwargs):
    print(kwargs)  # a dictionary of the keyword and value
#    for key, value in kwargs.items():
#        print(kwargs[key])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")  # Get will not return a error if the key does not exist, it returns None
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)

new_car = Car(make="Toyota", color="Red")
print(new_car.color)
print(new_car.model)  # No model was passed to Car so it will be None
