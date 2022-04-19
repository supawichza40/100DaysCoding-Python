with open("file1.txt") as file1:
    result1 = file1.readlines()
    result1 = [int(r.strip("\n")) for r in result1]

with open("file2.txt") as file2:
    result2 = file2.readlines()
    result2 = [int(r.strip("\n")) for r in result2]

print(result1,result2)
new_list = [num for num in result1 if num in result2]
print(new_list)
result =[]

# Write your code above 👆

print(result)


