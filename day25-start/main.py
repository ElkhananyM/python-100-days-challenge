# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# dict_data = data.to_dict()
# print(dict_data)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(int(data["temp"].mean()))
# print(data["temp"].max())

# print(data[data["day"] == "Monday"])

# print(data[data["temp"] == data["temp"].max()])

# monday = data[data["day"] == "Monday"]
# print(f"Temp in f: {monday["temp"] * (9 / 5) + 32}")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

squirrel_count = pandas.DataFrame(data_dict)
print(squirrel_count)

