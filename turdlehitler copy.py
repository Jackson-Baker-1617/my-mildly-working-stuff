from turtle import *

#create the loop doop
def superdooper():
    forward(10)
    left(90)
    forward(70)
    left(90)
    forward(70)
    left(90)
    forward(70)
    left(90)
    forward(10)
    left(90)
    forward(49)
    right(90)
    forward(48)
    right(90)
    forward(49)

#Move to the left
def rotation():
    penup()
    right(180)
    left(90)
    forward(129)
    right(90)
    forward(10)
    left(180)
    pendown()
#DO IT JUST DO IT DONT LET YOUR DREAMS BE DREAMS
def doit():
    for i in range(4):
        superdooper()
        rotation()
#actually running it
doit()
