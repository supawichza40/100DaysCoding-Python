def wrapper(function):
    def inner_function():
        print("Do Something Before")
        function()
        print("Do something after")
    return inner_function
def say_hello2():
    print("hello")

def say_hello():
    print("hello")

def inner_function(function):
    print("Do something beofre")
    function()
    print("Do somethinfg after")


# say_hello2()
# #or
# inner_function(say_hello)
#or
wrapper(say_hello2)()
#or
decorated_function = wrapper(say_hello2)
decorated_function()