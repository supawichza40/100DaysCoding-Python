import pandas
{"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]:row["code"] for index,row in nato_df.iterrows()}
nato_dict[" "] = "Spelling Surname"
print(nato_dict)
user_name = input("What is your name and surname? ")
user_name_list = [nato_dict[word] for word in user_name.upper()]
print(user_name_list)
