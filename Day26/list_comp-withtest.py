numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:
result = [item for item in numbers if item % 2 == 0]

#Write your code 👆 above:

print(result)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# Get names from names with 5 or more characters and add them to new list all uppercase

name_list = [name.upper() for name in names if len(name) >= 5]

print(name_list)


with open("file1.txt") as file1:
    file1_contents = file1.readlines()

with open("file2.txt") as file2:
    file2_contents = file2.readlines()

# Print the numbers which are in both file1.txt and file2.txt as ints.
results = [int(item) for item in file2_contents if item in file1_contents]

# Write your code above 👆

print(results)
