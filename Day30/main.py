
#FileNotFound
#with open("afile.txt") as file:
#   file.read()

# dictionary = {"key":"value"}
# try:
#     file = open("a_file.txt")
#     dictionary = {"key":"value"}
#     value = dictionary["key"]
#
# except FileNotFoundError as error_message:
#     print(f"There was an error: {error_message}. I will create it now.")
#     file = open("a_file.txt", "w")
#     file.write("Something")
#
# except KeyError as error_message:
#     print("That key does not exist.")
#     print(error_message)
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     file.close()


# Raise your own error
# rais

#keyError
#dictionary = {"key":"value"}
#value = dictionary["non_existent_key"]

#IndexError
#fruit_list = ["apple", "orange", "pear"]
#fruit = fruit_list[3]

#TypeError
#text = "abc"
#print(text + 5)

#Catching Exceptions
# try: Try this piece of code
# except: Do this if there was an exception
# else: Do this if there were no exceptions
# finally: Do this no matter what happens

# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)



