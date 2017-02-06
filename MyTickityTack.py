from turtle import *

speed(0)
pencolor('#4e2121')  # white
pensize(15)
title('Ticky')
setup(600, 600, 1300, 0)
# hideturtle()
bgcolor('#e2c59b')
penup()

# PENCOLOR FOR CIRCLE: #f23742 CROSS: #3e36f9

# Introduction


def gohidden(a):  # goto while penup
    penup()
    goto(a)
    pendown()


def printMap():  # prints board
    clear()
    pendown()
    gohidden((300, -100))
    for i in range(4):
        backward(600)
        forward(200)
        right(90)
        forward(200)


def mark(a, b):  # makes either an X or O. (a) is region, (b) is marking, either 1 for X or 2 for O
    region = [(), (-200, -200), (0, -200), (200, -200), (-200, 0), (0, 0), (200, 0), (-200, 200), (0, 200), (200, 200)]
    gohidden(region[a])
    pendown()
    if b is 1:
        lt(45)
        for i in range(4):
            lt(90)
            fd(75)
            gohidden(region[a])
        rt(45)
    else:
        rt(90)
        penup()
        fd(53)
        lt(90)
        pendown()
        circle(53)


printMap()
mark(5, 1)
mark(1, 2)
mark(9, 1)
mark(8, 2)
