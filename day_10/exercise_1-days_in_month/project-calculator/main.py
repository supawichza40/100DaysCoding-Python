import art
print(art.logo)

operation = ["+","-","*","/"]
def calculate(number1,number2,operation):
    if(operation=="+"):
        return number1+number2
    if(operation=="-"):
        return number1-number2
    if(operation=="*"):
        return number1*number2
    if(operation=="/"):
        return number1/number2
    else:
        return
    
continue_cal = True
user_number1 = float(input("What is the first number?"))
while(continue_cal):
    for oper in operation:
        print(oper)
    user_operation = input("Pick an operation: ")
    user_number2 = float(input("What is the next number?"))

    result = calculate(user_number1,user_number2,user_operation)
    print(f"{user_number1} {user_operation} {user_number2} = {result}")
    continue_cal = bool(int(input(f"type '1' to continue calculating with {result}, or  '0' to exit")))
    user_number1 = result