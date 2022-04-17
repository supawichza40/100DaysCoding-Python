import pandas
red_count = 0
grey_count = 0
black_count = 0
squirrel_data = pandas.read_csv("2018_squirrel.csv")
grey_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_count= len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_count_dict ={
    "Fur Color":["grey","red","black"],
    "Count":[grey_count,red_count,black_count]
}

squirrel_df = pandas.DataFrame(squirrel_count_dict)
squirrel_df.to_csv("squirrel_count.csv")