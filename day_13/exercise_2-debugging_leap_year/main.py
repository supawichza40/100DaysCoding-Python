year = int(input("Which year do you want to check?"))
#insert int since input will create a string but we using int to check for leap year.
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  