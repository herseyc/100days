

#with open("weather_data.csv") as file:
#    weatherlist = file.readlines()
#print(weatherlist)

#import csv

#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))

#print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

#print(type(data))

# print(data["temp"])

data_dict = data.to_dict()

print(data_dict)

temp_list = data["temp"].to_list()

print(temp_list)

# Calculate average without Pandas
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

# Using Pandas Series method to get mean Temp
print(data["temp"].mean())

# Using Pandas Series method to get max Temp
print(data["temp"].max())

# Getting Data in Columns
print(data["condition"])
# or
print(data.condition)

# Get Data in a Row
print(data[data.day == "Monday"])

# Get row with max temp
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(f"Monday Condition: {monday.condition}")

# Monday Temp and convert to F
print(f"{(int(monday.temp) * 9/5) + 32} F")

# create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

mydata = pandas.DataFrame(data_dict)
print(mydata)
mydata.to_csv("new_data.csv")

