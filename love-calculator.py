# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2

# convert names to lower case
names = combined_names.lower()

# use count to count the number of times a letter appears
t = names.count("t")
r= names.count("r")
u = names.count("u")
e = names.count("e")

true = t + r + u + e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

love = l + o + v + e

# Combine the two scores
total_score =  str(true) + str(love)

# Change the total score to an int
love_score = int(total_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


