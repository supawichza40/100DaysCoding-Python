from turtle import *
import random

shapey = Turtle()


side = 3
angle = [120,90,72,180-120,180-128.57,180-135,180-140,180-144]

for i in range(0,len(angle)):
    colormode(255)
    shapey.fillcolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    shapey.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    for j in range(0,side):
        shapey.forward(100)
        shapey.right(angle[i])
    side+=1

