import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

data_dict ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count,red_squirrels_count,black_squirrels_count ]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("Squirrel_Count.csv")






#####################################################################################################
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
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# sum_temp = 0
# for temp in temp_list:
#     sum_temp += temp

# len_temp_list = len(temp_list)
# sum_temp = sum(temp_list)
#
# avg_temp = sum_temp/len_temp_list
# print(avg_temp)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data.day =="Tuesday"])


#########################################################
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # max_temp = data.temp.max()
# # print(data[data.temp == max_temp])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp = monday_temp * 9 / 5 + 32
#
# print(monday_temp)

####################################################################################
# Create a dataframe from scratch
#
# import pandas
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores ": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data.to_csv("new_data.csv"))