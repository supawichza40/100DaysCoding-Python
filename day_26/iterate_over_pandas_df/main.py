student_dict = {
    "student":["Angela","James","Lily"],
    "score":[56,76,98]
}

import pandas
student_df = pandas.DataFrame(student_dict)
#loop through a dataframe in column
for key,val in student_df.items():
    print(key,val)
#loop through a df in row.
for (index,row) in student_df.iterrows():
    print(index,row)
