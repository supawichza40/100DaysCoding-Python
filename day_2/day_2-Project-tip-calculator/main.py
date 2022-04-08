print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip_percentage = input(
    "What percentage tip would you like to give? 10,12, or 15?")
number_of_people_to_split = input("How many people to split the bill?")
amount_each_people_pay = (
    float(total_bill)*(1+(float(tip_percentage)/100)))/float(number_of_people_to_split)
print(f"Each person should pay: ${round(amount_each_people_pay,2)}")
