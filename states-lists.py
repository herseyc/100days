states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(f"The second state in the list is: {states_of_america[1]}")

print(f"The last state in the list is: {states_of_america[-1]}")

#Alter an item in a list
print("Changing second state in the list.")
states_of_america[1] = "Pencilvania"
print(f"The second state in the list is now {states_of_america[1]}")

print(f"There are {len(states_of_america)} states in the list.")

#Add to the end of list
print("Adding a state to the end of the list.")
states_of_america.append("HerseyLand")
print(f"The last state on the list is now: {states_of_america[-1]}")
print(f"Now there are {len(states_of_america)} states in the list.")


#List of list
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# Separate list of fruits and vegetables
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Create a list of list in the pantry
pantry = [fruits, vegetables]

print(pantry)

print(f"There are {len(pantry)} shelves in the pantry")
print(f"There are {len(pantry[0])} fruits in the pantry.")
print(f"There are {len(pantry[1])} vegetables in the pantry.")

print(f"There are {pantry[0][2]} in the pantry.")

