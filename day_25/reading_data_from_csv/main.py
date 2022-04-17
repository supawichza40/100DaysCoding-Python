# with open("weather_data.csv") as file:
#     file = file.readlines()
#     for d in file:
#         print(d)
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file) # object created and we can loop to get each data
#     for d in data:
#         print(d)#list of row
import pandas

data_dict = {
    "students":["Amy","James","Angela"],
    "scores" :[76,56,65]

}
data = pandas.DataFrame(data_dict)
data.to_csv("test.csv")
print(data["students"])