import time
from turtle import *
from score import ScoreBoard
from paddle import Paddle
from ball import Ball


# Function
def draw_net():
    for _ in range(60):
        net.forward(10)
        net.penup()
        net.forward(10)
        net.pendown()


def is_game_on_func(ball):
    if ball.xcor() < -950:
        scoreboard.r_point()
        return False
    elif ball.xcor() > 950:
        scoreboard.l_point()
        return False
    else:
        return True


# variable
net_middle_cor = 0, -600
net_head_dir = 90
game_is_on = True

# Create instance object
# Create a screen
screen = Screen()
screen.bgcolor("black")
screen.screensize(canvheight=600, canvwidth=600)
screen.tracer(0)
screen.listen()
# create a net
net = Turtle()
net.pencolor("white")
net.fillcolor("white")
net.penup()
net.goto(net_middle_cor)
net.seth(net_head_dir)
draw_net()

# end net
# create score board
scoreboard = ScoreBoard()

# create a paddle
user_paddle = Paddle(-900)
# create a computer paddle
comp_paddle = Paddle(900)

# set up all events
screen.onkeypress(user_paddle.move_up, "w")
screen.onkeypress(user_paddle.move_down, "s")
while True:
    user_paddle.setup(-900)
    comp_paddle.setup(900)

    # create a new ball
    ball = Ball()
    while game_is_on:
        screen.update()
        comp_paddle.move_up_or_down_auto(ball.ycor())
        ball.is_forward_or_backward()
        scoreboard.update_scoreboard()
        if user_paddle.ycor() + 35 >= ball.ycor() >= user_paddle.ycor() - 35 and ball.xcor() <= -890:
            ball.change_ball_direction()
            ball.change_ball_heading_randomly()
        if comp_paddle.ycor() + 35 >= ball.ycor() >= comp_paddle.ycor() - 35 and ball.xcor() >= 890:
            ball.change_ball_direction()
            ball.change_ball_heading_randomly()

        ball.is_ball_touching_top()
        ball.is_ball_touching_bottom()
        game_is_on = is_game_on_func(ball)

        time.sleep(0.01)
    ball.hideturtle()
    ball.clear()

    game_is_on = True

screen.exitonclick()
