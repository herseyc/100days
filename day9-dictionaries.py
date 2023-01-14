programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

# printing a dictionary value
print(programming_dictionary["Function"])

#Adding to an existing dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

#Creat an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
#programming_dictionary = {}

#Edit item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"

print(programming_dictionary["Bug"])

#Looping through a dictionary
for key in programming_dictionary:
  print(key + " = " + programming_dictionary[key])