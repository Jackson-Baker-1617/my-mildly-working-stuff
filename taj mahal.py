from turtle import *

#create the loop doop
def superdooper():
    left(90)
    backward(10)
    left(90)
    backward(70)
    left(90)
    backward(70)
    left(90)
    backward(70)
    left(90)
    backward(10)
    left(90)
    backward(49)
    right(90)
    backward(48)
    right(90)
    backward(49)
    right(90)

#Move to the left
def rotation():
    penup()
    left(90)
    forward(45)
    left(180)
    pendown()
#DO IT JUST DO IT DONT LET YOUR DREAMS BE DREAMS
def doit():
    for i in range(4):
        superdooper()
        rotation()
#actually running it
doit()
