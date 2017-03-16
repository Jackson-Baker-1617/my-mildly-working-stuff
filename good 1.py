from turtle import *

# Variables ~ for ease of use
blu = '#1a64cc'  # 3e36f9garbage
red = '#cc1a2c'  # f23742
pale = '#000000'  # e2c59b
brow = '#2ce004'  # 4e2121
blac = '#2ce004'  # 262626
occupiedSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
xSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
oSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
currentTurn = 1  # 1 is X, 2 is O ~ X goes first, always
winCombos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


# turtle setup
speed(0)
pencolor(brow)
pensize(15)
title('Noughts and crosses good gentlemen')  # i dont know
setup(1920, 1000, 0, 0)
hideturtle()
bgcolor(pale)
penup()
Game = True


def reset():
    global Game, occupiedSpots, xSpots, oSpots, currentTurn
    clear()
    occupiedSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    xSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    oSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    currentTurn = 1
    pencolor(brow)
    pensize(15)
    Game = True


def gohidden(a):  # goto while penup
    penup()
    goto(a)
    pendown()


def setup():
    gohidden((0, 350))
    write("TIC TAC TOE", move=False, align="center", font=("DK Spiced Pumpkin", 70, "bold"))
    gamePrint("It's now X's turn.", blu)
    pencolor(blac)
    gohidden((700, -440))
    write("Click on the title to reset", move=False, align="center", font=("DK Spiced Pumpkin", 35, "bold"))
    gohidden((700, -470))
    write("Turtle will break if you go too fast. :P", move=False, align="center", font=("DK Spiced Pumpkin", 25, "bold"))


def printMap():  # prints board
    reset()
    pendown()
    gohidden((300, -100))
    for i in range(4):
        backward(600)
        forward(200)
        right(90)
        forward(200)
    setup()


def clearText():  # dedicated def to clear bottom text by painting over it
    pencolor(pale)
    pensize(120)
    gohidden((-400, -400))
    pendown()
    fd(650)
    penup()
    pensize(15)
    pencolor(brow)


def gamePrint(a, b):  # prints the current game text. (a) is text, (b) is color
    clearText()
    gohidden((0, -450))
    pencolor(b)
    write(a, move=False, align="center", font=("DK Spiced Pumpkin", 70, "bold"))


def mark(a, b, c, d):  # makes either an X or O. (a) is region, (b) is marking, either 1 for X or 2 for O, (c) is color, (d) is pensize
    region = [(-200, -200), (0, -200), (200, -200), (-200, 0), (0, 0), (200, 0), (-200, 200), (0, 200), (200, 200)]  # regions are marked based on numpad layout
    gohidden(region[a])
    pendown()
    pencolor(c)
    pensize(d)
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
    pensize(15)


def checkforwin():
    tiecount = 0
    global xSpots, oSpots, occupiedSpots, winCombos, Game
    for i in winCombos:
        if xSpots[i[0]] == xSpots[i[1]] == xSpots[i[2]] == 0:
            print("x wins")
            for u in range(0, 9):
                if xSpots[u] == 0:
                    mark(u, 1, blac, 30)
                    mark(u, 1, blu, 15)
            gamePrint("X wins.", blu)
            Game = False
            return
        if oSpots[i[0]] == oSpots[i[1]] == oSpots[i[2]] == 0:
            print("o wins")
            for u in range(0, 9):
                if oSpots[u] == 0:
                    mark(u, 2, blac, 30)
                    mark(u, 2, red, 15)
            gamePrint("O wins.", red)
            Game = False
            return

    for o in range(0, 9):
        if occupiedSpots[o] == 0:
            tiecount += 1
        if tiecount == 9:
            print("cat")
            gamePrint("TIE.", blac)
            Game = False
            return


def checkValid(a):  # make sure the selected spot hasnt been marked already
    global occupiedSpots
    if occupiedSpots[a] == 0:
        return False
    else:
        occupiedSpots[a] = 0
        return


def markData(a):  # input the newly selected region into the data and run checkforwin
    global xSpots, oSpots, currentTurn
    if currentTurn == 1:
        xSpots[a] = 0
        mark(a, 1, blu, 15)
        currentTurn = 2
        gamePrint("It's now O's turn.", red)
    else:
        oSpots[a] = 0
        mark(a, 2, red, 15)
        currentTurn = 1
        gamePrint("It's now X's turn.", blu)
    checkforwin()


def deterReg(x, y):  # determines the region where the player clicked
    global Game
    if Game is False or y >= 350:
        printMap()
        return
    if x >= -300 and x <= -100:  # places 1, 4, 7
        if y >= -300 and y <= -100: regionPos = 0
        elif y >= -100 and y <= 100: regionPos = 3
        elif y >= 100 and y <= 300: regionPos = 6
        else: regionPos = 9  # couldn't be determined
    elif x >= -100 and x <= 100:  # places 2, 5, 8
        if y >= -300 and y <= -100: regionPos = 1
        elif y >= -100 and y <= 100: regionPos = 4
        elif y >= 100 and y <= 300: regionPos = 7
        else: regionPos = 9  # couldn't be determined
    elif x >= 100 and x <= 300:  # places 3, 6, 9
        if y >= -300 and y <= -100: regionPos = 2
        elif y >= -100 and y <= 100: regionPos = 5
        elif y >= 100 and y <= 300: regionPos = 8
        else: regionPos = 9  # couldn't be determined
    else: regionPos = 9  # couldn't be determined
    if regionPos != 9:  # if the player hasn't selected a nonregion, continue
        if checkValid(regionPos) is not False:
            markData(regionPos)


printMap()
onscreenclick(deterReg)

# ~ Daniel Eastman, 2017
# ~I DID SOME COLOURING - JACKSON

