from turtle import *
import random
import time
path = '/users/Jackson/gregory.txt'
grt= open(path)
text= grt.read().strip().split()
baltic = ["russia","ukraine","belarus","uzbekistan","kazakhstan","georgia","azerbaijan","lithuania","moldova","latvia","kyrgyzstan","tajikistan","armenia","turkmenistan","estonia"]
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
def new():
    ech=input("are you new? (y/n) ")
    if ech=="y":
        setup()
    elif ech=="n":
        reallog()
def setup():
    gregory_file = open(path,'w')
    name1=input("what is your name? ")
    password1=input("now what do you want to make your password? ")
    passwordcheck=input("Confirm that password please ")
    if passwordcheck==password1:
        print("great! now were set up")
        print("Welcome,",name1)
        gregory_file.write(name1.lower()+"\n")
        gregory_file.write(password1.lower()+"\n")
        reallog()
    else:
        print("You've already lost this game and it didnt even start yet")
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
def reallog():
    while True:
        namecheck=input("what was your username? ")
        if namecheck in text:
            passcheck=input("what was your password? ")
            if passcheck in text:
                print("Welcome back,",namecheck)
                first()
            else:
                break
        else:
            break
def first():
    start=input("play game?(y/n)")
    if start.lower()=="y":
            game()
    elif start.lower()=="n":
            print ("You moist golfball")
def game():
    gregory_file = open(path,'w')
    print("guess the former USSR states with no hints until you eventually lose(or reach maximum score of 10)")
    a1=input("first state")
    if a1.lower()==b1:
        a2=input("next state")
        if a2.lower()==b2:
            a3=input("next state")
            if a3.lower()==b3:
                  print("congrats")
                  gregory_file.write("3"+"\n")
            else:
                print ("You moist golfball")
                gregory_file.write("2"+"\n")
        else:
            print ("You moist golfball")
            gregory_file.write("1"+"\n")
    else:
        print ("You moist golfball")
        gregory_file.write("0"+"\n")

new()
