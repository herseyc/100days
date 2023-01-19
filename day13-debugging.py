############DEBUGGING#####################

# # Describe Problem
def my_function():
#The range function does not include end entry
# for i in range(1, 20): Will never get to 20
 for i in range(1, 21):
   if i == 20:
     print("You got it")
my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#randit function includes the start and end.  If set to (1, 6) if 6 is selected it will be
#be out of range of the list index
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# # Play Computer
# If you enter 1994 it will not id you as GenZ.  Need to add >= so the elif statement is True if you
# enter 1994
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")
# I added this to catch everything earlier than 1980, since we are old
else:
  print("You are old.")

# # Fix the Errors
age = int(input("How old are you?"))
if age > 18:
 print(f"You can drive at age {age}.")

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
#Uncomment to debug
# print(f"Pages: {pages}")
#print(f"Words per page {word_per_page}")

total_words = pages * word_per_page
print(total_words)

# #Use a Debugger - ie https://pythontutor.com/visualize.html#mode=edit
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # appending to b_list was outside the for loop so only the last item was added to the list.
  print(b_list)

mutate([1,2,3,5,8,13])