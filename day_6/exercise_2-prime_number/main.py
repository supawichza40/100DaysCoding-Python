# Write your code below this line 👇
def prime_checker(number):
    for num in range(number-1, 1, -1):
        if(number % num == 0):
            print("It's not a prime number.")
            return

    print("It's a prime number.")
    return


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
