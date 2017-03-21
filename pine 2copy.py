from turtle import *
import random
import time
starty=input("Are you returning or are you new? (new/old)")
if starty.lower()=="new":
    nameo=input("Lets begin with your name: ")
    textname=nameo+".txt"
    with open (textname, "a+") as file:
        file.write(nameo.lower()+"\n")
    boyo=input("Choose a password: ")
    with open (textname, "a+") as file:
        file.write(boyo.lower()+"\n")
elif starty.lower()=="old":
    print("Welcome back")
