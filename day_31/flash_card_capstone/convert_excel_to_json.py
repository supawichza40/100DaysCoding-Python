import json

import pandas
lang_dict = []


data = pandas.read_csv(filepath_or_buffer="data/french_words.csv")
for index,row in data.iterrows():
    lang_dict.append({
        "English":row["English"],
        "French":row["French"]
    })
with open("lang.json",mode="w") as writer:
    json.dump(lang_dict,writer,indent=4)

