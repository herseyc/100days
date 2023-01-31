sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {letter: len(letter) for letter in sentence.split()}

print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
weather_f = {day: (ctemp * 9/5) + 32 for (day, ctemp) in weather_c.items() if ctemp > 20}


# Write your code 👇 below:

print(weather_f)
