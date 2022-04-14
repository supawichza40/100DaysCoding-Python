from turtle import Turtle, Screen
import random
def set_turtle_to_start(turtle,x,y,speed,color):
    turtle.shape("turtle")
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.speed(speed)
def create_finish_line():
    finish_line.penup()
    finish_line.goto(400, 400)
    finish_line.pendown()
    finish_line.right(90)
    finish_line.forward(1000)
speed = 10
red = Turtle()
orange = Turtle()
yellow = Turtle()
green = Turtle()
blue = Turtle()
violet = Turtle()

screen = Screen()
finish_line = Turtle()

set_turtle_to_start(red,-400,-300,speed,"red")
set_turtle_to_start(orange,-400,-200,speed,"orange")
set_turtle_to_start(yellow,-400,-100,speed,"yellow")
set_turtle_to_start(green,-400,0,speed,"green")
set_turtle_to_start(blue,-400,100,speed,"blue")
set_turtle_to_start(violet,-400,200,speed,"violet")
user_bet = screen.textinput(title="Make your bet",prompt="Who will win the race? Enter a colour: ")
create_finish_line()

while(red.xcor()<=400 and orange.xcor()<=400  and yellow.xcor()<=400 and green.xcor()<=400and blue.xcor()<=400and violet.xcor()<=400):
    red.forward(random.randint(0,10))
    orange.forward(random.randint(0,10))
    yellow.forward(random.randint(0,10))
    green.forward(random.randint(0,10))
    blue.forward(random.randint(0,10))
    violet.forward(random.randint(0,10))

if((user_bet=="red" and red.xcor()>=400) or (user_bet=="orange" and orange.xcor()>=400) or (user_bet=="yellow" and yellow.xcor()>=400) or (user_bet=="green" and green.xcor()>=400)or (user_bet=="blue" and blue.xcor()>=400) or (user_bet=="violet" and violet.xcor()>=400) ):
    screen.textinput(title="Result",prompt="YOU ARE A WINNER!")
    print("You are a winner")
else:
    screen.textinput(title= "Result",prompt="YOU LOSE")





screen.exitonclick()