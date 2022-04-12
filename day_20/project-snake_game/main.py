from turtle import Turtle,Screen
import random
import snake


snake_obj = snake.Snake()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("grey")


#Move the snake
#move snake across the screen

def turn_up():

    snake_obj.snake[0].seth(90)
def turn_down():

    snake_obj.snake[0].seth(270)
def turn_right():

    snake_obj.snake[0].seth(0)
def turn_left():

    snake_obj.snake[0].seth(180)


screen.listen()
screen.onkey(fun=turn_up, key="w")
screen.onkey(fun=turn_down, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")


while(not snake_obj.is_head_touching_body() and not snake_obj.is_snake_outside_game()):
    snake_obj.forward()

    snake_obj.is_snake_eating_dot()
screen.exitonclick()