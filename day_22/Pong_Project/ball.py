from turtle import Turtle
import random

ball_move_amount = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1)
        self.fillcolor("white")
        self.pencolor("white")
        self.ball_direction = 0
        self.paddle_degree = [280, 440]

    def move_ball_backward(self):
        self.backward(ball_move_amount)

    def move_ball_forward(self):
        self.forward(ball_move_amount)

    def is_forward_or_backward(self):
        if self.ball_direction == 0:
            self.move_ball_backward()
        else:
            self.move_ball_forward()

    def change_ball_direction(self):
        if self.ball_direction == 0:
            self.ball_direction = 1
        else:
            self.ball_direction = 0

    def is_ball_touching_top(self):
        if self.ycor() > 500:
            if self.ball_direction == 1:
                self.seth(315)
            else:
                self.seth(45)

    def is_ball_touching_bottom(self):
        if self.ycor() < -500:
            if self.ball_direction == 1:
                self.seth(45)
            else:
                self.seth(315)

    def change_ball_heading_randomly(self):
        self.seth(random.randint(self.paddle_degree[0], self.paddle_degree[1]))
