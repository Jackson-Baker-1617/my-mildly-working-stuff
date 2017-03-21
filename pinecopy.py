from turtle import *
import random
import time
start=input("Are you new? yes/no ")
if start.lower()=="yes":
    name=input("Lets begin with your name: ")
    with open (gregory.txt, "a+") as file:
        file.write(nameo.lower()+"\n")
    boyo=input("Choose a password: ")
    with open (gregory.txt, "a+") as file:
        file.write(boyo.lower()+"\n")
        confirm=input("Confirm password: ")
    with open (gregory.txt, "a+") as file:
        file.write(boyo.lower()+"\n")
elif start.lower()=="no":
    print("Welcome back")
    checker=input("what's your name again?")
    with open("gregory.txt", "r+") as file: 
        filecontents=file.read() 
