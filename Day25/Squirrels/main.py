import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get number of each color of squirrels
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])


squirrel_counts = {
    "Fur Color": ["Black", "Gray", "Red"],
    "Counts": [black_squirrels_count, gray_squirrels_count, red_squirrels_count]
}

#print(squirrel_counts)

squirrel_data = pandas.DataFrame(squirrel_counts)
squirrel_data.to_csv("squirrelcounts.csv")
#print(squirrel_data)
