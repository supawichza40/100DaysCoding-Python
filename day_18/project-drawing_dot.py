import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
def draw():
    tim.pendown()
    tim.circle(0)

def draw_one_line_of_dot():
    for _ in range(16):
        tim.fillcolor(random_color())
        tim.pencolor(random_color())
        draw()
        tim.penup()
        tim.forward(50)
def move_to_next_ready_position(level):
    tim.penup()
    tim.goto(-400,-300+(shift_up_amount*level))

tim.speed(0)
#POSITION IS RELATIVE, MEANING DOES NOT DEPEND ON THE ARROW
start_position = (-400,-300)
shift_up_amount = 50
tim.penup()
tim.goto(start_position)
tim.pensize(15)

for level in range(15):
    draw_one_line_of_dot()
    move_to_next_ready_position(level)
t.exitonclick()

