import random
#Old way doing dict
names = ["Alex","Daniel","Money","Robert"]
student_dict = {}
#normal dictionary
for student in names:
    student_dict[student] = random.randint(0,5)
print(student_dict)

#List comprehension
student_dict2 = {student:random.randint(0,5) for student in names}
print(student_dict2)