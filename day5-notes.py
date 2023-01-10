# Loops execute multiple times

fruits = ["Apple", "Peach", "Pear"]

# loop through a list
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# loop through range
# range does not include last number so 1-10 would be 1, 11
for number in range(1, 11):
    print(number)

# add steps
for number in range(1, 11, 3):
    print(number)

# add all numbers in a range together
total = 0
for number in range(1, 101):
    total += number

print(total)

# add only the even numbers
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

# FizzBuzz

# Write your code below this row 👇
for number in range(1, 101):
    # if divisible by 3 and 5 print FizzBuzz
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # if divisible by 3 print Fizz
    elif number % 3 == 0:
        print("Fizz")
    # if divisible by 5 print Buzz
    elif number % 5 == 0:
        print("Buzz")
    # otherwise just print the number
    else:
        print(number)