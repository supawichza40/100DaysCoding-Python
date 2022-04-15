from turtle import Turtle, Screen

# registering rectangle shape, so we can use it as our pen.
screen = Screen()
screen.register_shape("rectangle", ((10, -35), (10, 35), (-10, 35), (-10, -35)))
paddle_move_amount = 40


class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.penup()
        self.pencolor("white")
        self.fillcolor("white")
        self.shape("rectangle")
        self.goto(x_cor, 0)
        self.seth(90)

    def setup(self, x_cor):
        self.clear()
        self.goto(x_cor, 0)
        self.seth(90)

    def move_up(self):
        self.forward(paddle_move_amount)
        self.seth(90)

    def move_down(self):
        self.backward(paddle_move_amount)
        self.seth(90)

    def move_up_or_down_auto(self, ball_pos_y):
        if ball_pos_y > self.ycor():
            self.move_up()
        elif ball_pos_y <= self.ycor():
            self.move_down()
        else:
            return
