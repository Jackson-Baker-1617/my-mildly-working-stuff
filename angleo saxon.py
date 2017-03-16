from turtle import *
#gotta go fast by making speed 0
speed(0)
#makes the color better and changeable
colormode(255)
#PINK COLOR
pencolor(255,0,255)
#makes the box for the swiss flag and kills all the jedi
def order66():
    right(90)
    forward(66)
    right(90)
    forward(66)
    left(90)
    forward(66)
#makes it loop to become swiss
def loopdeloop():
    for i in range(4):
        order66()
#makes it turn
def NOWTURNIT():
    loopdeloop()
    circle(0,90)
#loops it 4 times for the desiered swill quadri
for i in range(4):
    NOWTURNIT()
