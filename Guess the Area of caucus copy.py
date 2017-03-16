from turtle import *
import random
import time

asia = ["JohnWetton","Tibet"," Siberia"]

#first def class
def worm():
    rice=random.choice(asia)
    bgcolor('#6f1b72')
    pencolor('#85b25b')
    write(rice, font=("Comic Sans",100))
    time.sleep(1)
    reset()
    penup()
    goto(-250, 0)
    write("ASIA TIME LETS DO THIS FRIEND", font=("Times New Roman",45))
    
          
worm()
