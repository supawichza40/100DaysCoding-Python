for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: #this will take either not both since using or.
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:#if else is wrong, if there is only one outcome, connect by elif
    print(number)#there is []which will get printed as list,remove it