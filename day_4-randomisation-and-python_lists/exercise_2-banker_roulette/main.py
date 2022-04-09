# 🚨 Don't change the code below 👇
import random as random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_people_number = random.randint(0,len(names)-1)
print(f"{names[random_people_number]} is going to buy the meal today!")