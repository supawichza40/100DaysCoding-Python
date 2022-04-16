file = open(file="my_file.txt",mode="a")#open file and save in file variable
#this is equivalent to above
with open("my_file.txt",mode="a") as f:
    f.write("TEst")
    f.writelines("Text")