from turtle import *
speed(0)
#Make the side open box
def box():
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
#makes the backsquare
def square():
    penup()
    left(90)
    forward(10)
    forward(10)
    pendown()
    right(90)
    forward(20)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(30)
#runs it 4 times
def doitagain():
    for i in range(4):
        box()
#actually creates the swiss flag
doitagain()
square()
