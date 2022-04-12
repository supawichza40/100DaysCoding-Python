import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turn = ["right","left"]
angle = 90
direction = ["forward","backward"]
tim.speed(0)
tim.pensize(15)
for _ in range(100000):
    tim.fillcolor(random.choice(colours))
    tim.pencolor(random.choice(colours))
    direct = random.choice(direction)
    if(direct=="forward"):
        tim.forward(random.randint(0,100))
    else:
        tim.backward(random.randint(0,100))
    turning = random.choice(turn)
    if(turning=="right"):
        tim.right(angle)

    else:
        tim.left(angle)

t.exitonclick()