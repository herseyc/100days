# Working with files

# Open and read
#open the file
file = open("my_file.txt")
# read the contents of the file
contents = file.read()
# print the contents
print(contents)
# close the file
file.close()

# Use with will close the file when done
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Overwrites
#with open("my_file.txt", mode="w") as file:
#    file.write("New Text.")

# Appending
with open("my_file.txt", mode="a") as file:
    file.write("\nNew Text.")

# Write will create the file if it does not exist and it will overwrite the contents of the file
# Use mode="a" to append to a file
with open("new_file.txt", mode="w") as file:
    file.write("This is a new file")










