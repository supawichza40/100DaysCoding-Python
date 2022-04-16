from turtle import Turtle, Screen
import random


class Snake:
    def __init__(self):
        self.score = 0
        self.snake = []
        self.error_rate = 10
        self.high_score = 0
        self.score_gui = self.update_score()
        self.random_circle = self.generate_random_circle()

        for _ in range(3):
            segment = Turtle()
            segment.penup()
            segment.color("white")
            segment.shape("square")
            segment.goto(len(self.snake) * -10, 0)
            self.snake.append(segment)
    def restart(self):
        if self.score>self.high_score:
            self.high_score = self.score
        self.score = 0
        for i in range(len(self.snake)):
            self.snake[i].clear()
        self.snake = []
        for _ in range(3):
            segment = Turtle()
            segment.penup()
            segment.color("white")
            segment.shape("square")
            segment.goto(len(self.snake) * -10, 0)
            self.snake.append(segment)

    def save_high_score_to_file(self):
        with open("high_score.txt","w") as high_score:
            high_score.write(str(self.high_score))

    def read_high_score_from_file(self):
        with open("high_score.txt","r") as high_score:
            content = high_score.read()
            if(content!=""):
                self.high_score = int(content)
            else:
                pass


    def add_new_snake_segment(self):
        for _ in range(1):
            segment = Turtle()
            segment.penup()
            segment.color("white")
            segment.shape("square")
            segment.goto(self.snake[len(self.snake) - 1].pos())
            self.snake.append(segment)

    def generate_random_circle(self):
        dot_position = (random.randint(-250, 250), random.randint(-250, 250))
        dot = Turtle()
        dot.penup()
        dot.shape("circle")
        dot.goto(dot_position)
        return dot

    def forward(self):

        for index in range(len(self.snake) - 1, 0, -1):
            pos_x = self.snake[index - 1].xcor()
            pos_y = self.snake[index - 1].ycor()
            self.snake[index].goto(pos_x, pos_y)
        self.snake[0].forward(10)

    def is_head_touching_body(self):
        for index in range(1, len(self.snake) - 1, 1):
            if (self.snake[0].xcor() + self.error_rate > self.snake[index].xcor() and self.snake[
                0].xcor() - self.error_rate < self.snake[
                index].xcor() and self.snake[0].ycor() + self.error_rate > self.snake[index].ycor() and self.snake[
                0].ycor() - self.error_rate <
                    self.snake[index].ycor()):
                print("Body touching")
                return True
        return False

    def is_snake_outside_game(self):
        if (self.snake[0].xcor() > 300 or self.snake[0].xcor() < -300 or self.snake[0].ycor() > 400 or self.snake[
            0].ycor() < -400):
            return True
        else:
            return False

    def update_score(self):
        style = ('Courier', 30, 'italic')
        timmy = Turtle()
        timmy.color("deep pink")
        timmy.write(f'Score: {self.score} HighScore:{self.high_score}', font=style, align='center')
        timmy.hideturtle()
        return timmy
    def is_snake_eating_dot(self):
        if (self.snake[0].xcor() + self.error_rate > self.random_circle.xcor() and self.snake[
            0].xcor() - self.error_rate < self.random_circle.xcor() and self.snake[
            0].ycor() + self.error_rate > self.random_circle.ycor() and self.snake[
            0].ycor() - self.error_rate < self.random_circle.ycor()):
            self.score += 1
            self.random_circle.hideturtle()
            self.score_gui.clear()
            self.add_new_snake_segment()
            self.random_circle = self.generate_random_circle()
            self.score_gui = self.update_score()
            return True
        else:
            False


