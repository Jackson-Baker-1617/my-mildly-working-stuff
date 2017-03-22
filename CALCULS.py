from tkinter import*
greg=Tk()
greg.geometry("50000x50000")
def ded():
    global shrek
    shrek=[ ]
def on():
    showoff.config(text="")
def off():
    quit()
def 1():
    showoff.config(text="1")
    shrek.append("1")
def 2():
    showoff.config(text="2")
    shrek.append("2")
def 3():
    showoff.config(text="3")
    shrek.append("3")




ded()

showoff=Label(text="000000000")
showoff.place(x=700, y=700)

on=Button(text="ON/C", command=on)
on.place(x=10, y=10)

off=Button(text="OFF", command=off)
off.place(x=100, y=10)

1=Button(text="1", command=1)
1.place(x=10, y=50)

2=Button(text="2", command=2)
2.place(x=100, y=50)

3=Button(text="3", command=3)
3.place(x=200, y=50)
