from turtle import *

tim = Turtle()
def forward():
    tim.forward(5)

def backward():
    tim.backward(5)

def clockwise():
    tim.right(5)
def anti_clockwise():
    tim.left(5)


screen = Screen()
screen.listen()
screen.onkeypress(fun=backward,key = "s")
screen.onkeypress(fun=clockwise,key="d")
screen.onkeypress(fun=anti_clockwise,key="a")
screen.onkeypress(fun=forward,key = "w")
screen.exitonclick()