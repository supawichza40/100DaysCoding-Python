fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]

try:

    make_pie(4)
except IndexError as message_error:
    print(f"Invalid {message_error}")
    print("Fruit pie")
else:
    print(fruit + " pie")


