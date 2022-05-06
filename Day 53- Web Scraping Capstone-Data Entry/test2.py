def wrapper(function):
    def inner_function():
        print("Do Something Before")
        function()
        print("Do something after")
    return inner_function


def say_hello():
    print("hello")
say_hello()

def inner_function(function):
    print("Do something beofre")
    function()
    print("Do somethinfg after")


inner_function(say_hello)