from turtle import Turtle

dashy = Turtle()
def singleLineDashAndBack():
    for i in range(0,20):
        dashy.pd()
        dashy.forward(5)
        dashy.pu()
        dashy.forward(5)

singleLineDashAndBack()
