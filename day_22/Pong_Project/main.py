import time
import turtle
from turtle import *
import sys
import random
screen = Screen()

screen.bgcolor("black")
screen.screensize(canvheight=600,canvwidth=600)
screen.tracer(0)
#net
net = Turtle()
net.pencolor("white")
net.fillcolor("white")
net.penup()
net.goto(0,-600)
net.seth(90)
for _ in range(60):
    net.forward(10)
    net.penup()
    net.forward(10)
    net.pendown()
#end net
#create a paddle

user_paddle = Turtle()
user_paddle.penup()
user_paddle.pencolor("white")
user_paddle.fillcolor("white")
screen.register_shape("rectangle", ((10,-35),(10,35), (-10,35), (-10,-35)))
user_paddle.shape("rectangle")
user_paddle.goto(-900,0)

#create a computer paddle
comp_paddle = Turtle()
comp_paddle.penup()
comp_paddle.fillcolor("white")
comp_paddle.pencolor("white")
comp_paddle.shape("rectangle")
comp_paddle.goto(900,-200)
comp_paddle.forward(10)
comp_paddle.seth(90)
def move_up():

    user_paddle.forward(10)
    user_paddle.seth(90)


def move_down():
    user_paddle.backward(10)
    user_paddle.seth(90)

#create a paddle event
screen.listen()


#create a ball
ball = Turtle()
ball.shape("square")
ball.shapesize(1)
ball.fillcolor("white")
ball.pencolor("white")


def move_ball_backward():
    ball.backward(10)

#create a bouncing ball
def move_ball_forward():
    ball.forward(10)

ball_direction = 0#0=backward, 1= forward
def is_forward_or_backward(ball_direction):
    if(ball_direction==0):
        move_ball_backward()
    else:
        move_ball_forward()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
game_is_on = True
user_paddle_degree = [280,440]
while(game_is_on):
    screen.update()

    is_forward_or_backward(ball_direction)
    if(ball.ycor()<=user_paddle.ycor()+35 and ball.ycor()>=user_paddle.ycor()-35 and ball.xcor()<=-890):
        ball_direction = 1
        ball.seth(random.randint(user_paddle_degree[0],user_paddle_degree[1]))
    if(ball.ycor()<=comp_paddle.ycor()+35 and ball.ycor()>=comp_paddle.ycor()-35 and ball.xcor()>=890):
        ball_direction = 0
        ball.seth(random.randint(user_paddle_degree[0],user_paddle_degree[1]))
    if(ball.ycor()>500):
        if(ball_direction==1):
            ball.seth(315)
        if(ball_direction==0):
            ball.seth(45)

    if(ball.ycor()<-500):
        if(ball_direction==1):
            ball.seth(45)
        if(ball_direction==0):
            print("I am test")
            ball.seth(315)


    time.sleep(0.01)

screen.exitonclick()