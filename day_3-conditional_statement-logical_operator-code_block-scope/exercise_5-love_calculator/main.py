# 🚨 Don't change the code below 👇
from numpy import number


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_t = int(name1.lower().count("t")+name2.lower().count("t"))
number_r = int(name1.lower().count("r")+name2.lower().count("r"))
number_u = int(name1.lower().count("u")+name2.lower().count("u"))
number_e = int(name1.lower().count("e")+name2.lower().count("e"))

number_l = int(name1.lower().count("l")+name2.lower().count("l"))
number_o = int(name1.lower().count("o")+name2.lower().count("o"))
number_v = int(name1.lower().count("v")+name2.lower().count("v"))

first_digit_sum = number_t + number_r +number_u +number_e
second_digit_sum = number_l + number_o + number_v + number_e

sum = int(str(first_digit_sum)+str(second_digit_sum))

if(sum<10 or sum>90):
    print(f"Your score is {sum}, you go together like coke and mentos.")
elif(sum>=40 and sum<=50):
    print(f"Your score is {sum}, you are alright together.")
else:
    print(f"Your score is {sum}.")

