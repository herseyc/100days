import random

#random int between 1 - 10
a = random.randint(1,10)
print(f"This is a random int between 1 and 10: {a}")

#random float 0 to almost 1
b = random.random()
print(f"This is a random float: {b}")

#Taking random which is a float between 0 and almost 1 and making it between 0 and almost 5
d = b * 5
print(f"This is the random float * 5: {d}")

#random float to int 0-5
#rounding should catch the 5
c = int(round(d))
print(f"This is using the random float to create a random int between 0 and 5: {c}")


# Use random.choice to choose an item in a list at random
list_of_stuff = ["Hello", "Good Bye", "Nice to See You", "Been a While"]
greeting = random.choice(list_of_stuff)
print(greeting)

