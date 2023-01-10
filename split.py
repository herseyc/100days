

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#create a list of individual characters from a string
alphabet_list = [*alphabet]

print(alphabet_list)

# Use split to split a space delimited string
numbers = "1 2 3 4 5 6 7 8 9 0"

numbers_list = numbers.split()

print(numbers_list)

# Use split with a comma (,) delimiter
comma = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50"
num_list = comma.split(", ")
print(num_list)