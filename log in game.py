#just leftover from essentially copy and pasted last game. but made unfair
from turtle import *
import random
import time
#one source i cant remember taught me how to do this path thing
path = '/Users/jacksonbaker/Desktop/gregory.txt'
grt= open(path)
text= grt.read().strip().split()
#former USSR states
baltic = ["russia","ukraine","belarus","uzbekistan","kazakhstan","georgia","azerbaijan","lithuania","moldova","latvia","kyrgyzstan","tajikistan","armenia","turkmenistan","estonia"]
#orininally i was going to have you guess ten. then i grew a soul
b1=(random.choice(baltic))
b2=(random.choice(baltic))
b3=(random.choice(baltic))
b4=(random.choice(baltic))
b5=(random.choice(baltic))
b6=(random.choice(baltic))
b7=(random.choice(baltic))
b8=(random.choice(baltic))
b9=(random.choice(baltic))
b10=(random.choice(baltic))
#def to start it off
def new():
    ech=input("are you new? (y/n) ")
    if ech=="y":
        setup()
    elif ech=="n":
        reallog()
#def to make an account
def setup():
    while True:
        gregory_file = open(path,'a+')
        name1=input("what is your name new player? ")
        password1=input("now what do you want to make your password? ")
        passwordcheck=input("Confirm that password please ")
        if passwordcheck==password1:
            print("great! now were set up")
            print("Welcome,",name1, "Please reset program and relog to continue(go to shell and hit f5)")
            gregory_file.write(name1.lower()+"\n")
            gregory_file.write(password1.lower()+"\n")
            break
        else:
            print("You've already lost this game and it didnt even start yet")
#def to login(original and cut)
def login():
        gregory_file = open(path,'r')
        with open(gregory_file):    
            usercheck=input("What was your username?")
            if usercheck == line.split():
                passcheck=input("So what was the password there?")
                if passcheck == line.split():
                    print("Welcome back", usercheck)
                else:
                    print("Looks like you messed up the password there bud")
            else:
                print("seems you aren't registered. do that now")

#new login def
def reallog():
    while True:
        namecheck=input("what was your username? ")
        if namecheck in text:
            passcheck=input("what was your password? ")
            if passcheck in text:
                print("Welcome back,",namecheck)
                first()
            else:
                print("Looks like you messed up the password there bud")
                reallog()
        else:
            print("seems you aren't registered. do that now")
            setup()
            break
#def to actually start game
def first():
    start=input("play game?(y/n)")
    if start.lower()=="y":
            game()
    elif start.lower()=="n":
            print ("You moist golfball")
#pretty much the entire game
def game():
    gregory_file = open(path,'a')
    print("guess the random former USSR states with no hints until you eventually lose(or reach maximum score of 3)")
    a1=input("first state: ")
    if a1.lower()==b1:
        a2=input("next state: ")
        if a2.lower()==b2:
            a3=input("last state: ")
            if a3.lower()==b3:
                  print("Nice. you got all three")
                  gregory_file.write("3"+"\n")
                  reset()
            else:
                print ("I guess you got two")
                gregory_file.write("2"+"\n")
                print("Current record: 0")
                reset()
        else:
            print ("You only got one")
            gregory_file.write("1"+"\n")
            print("Current record: 0")
            reset()
    else:
        print ("You didn't even get one")
        gregory_file.write("0"+"\n")
        print("Current record: 0")
        reset()
#def to restart
def reset():
    while True:
        setergegrstart=input("Retry? Yes, I am aware this game is cheap and unfair.(y/n)")
        if setergegrstart.lower()=="y":
                game()
        elif setergegrstart.lower()=="n":
                print ("You lizard ball")
        else:
            print("i hate you")
            break
#to make it work
new()
#python for beginners was a fantastic source and helpful. 100% reccoment
