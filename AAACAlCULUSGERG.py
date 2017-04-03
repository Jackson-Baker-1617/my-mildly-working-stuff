from tkinter import*
import webbrowser
greg=Tk()
greg.geometry("300x500")
greg.configure(background='pink')
def ded():
    global shrek
    shrek=0
    global lasaga
    lasaga=0
    global plus
    plus = False
    global devide
    devide = False
    global multi
    multi = False
    global submis
    submis = False
def on():
    global shrek, lasaga, plus, devide, multi, submis
    shrek = 0
    lasaga = 0
    plus = False
    devide = False
    multi = False
    submis = False
    showoff.config(text="")
def off():
    quit()
def un():
    showoff.config(text=showoff.cget("text") + "1")
def dos():
    showoff.config(text=showoff.cget("text") + "2")
def tres():
    showoff.config(text=showoff.cget("text") + "3")
def quad():
    showoff.config(text=showoff.cget("text") + "4")
def sink():
    showoff.config(text=showoff.cget("text") + "5")
def six():
    showoff.config(text=showoff.cget("text") + "6")
def sept():
    showoff.config(text=showoff.cget("text") + "7")
def huit():
    showoff.config(text=showoff.cget("text") + "8")
def neuf():
    showoff.config(text=showoff.cget("text") + "9")
def nda():
    showoff.config(text=showoff.cget("text") + "0")
def add():
    global plus, shrek
    shrek = showoff.cget("text")
    plus = True
    showoff.config(text="")
def sub():
    global submis, shrek
    shrek = showoff.cget("text")
    submis = True
    showoff.config(text="")
def div():
    global devide, shrek
    shrek = showoff.cget("text")
    devide = True
    showoff.config(text="")
def times():
    global multi, shrek
    shrek = showoff.cget("text")
    multi = True
    showoff.config(text="")
def equal():
    global shrek
    lasaga = showoff.cget("text")
    shrek = float(shrek)
    lasaga = float(lasaga)
    if plus is True:
        gregleg = shrek + lasaga
        showoff.config(text=gregleg)
    elif submis is True:
        greenbeen = shrek - lasaga
        showoff.config(text=greenbeen)
    elif devide is True:
        america = shrek / lasaga
        showoff.config(text=america)
    elif multi is True:
        sloth = shrek * lasaga
        showoff.config(text=sloth)
def decimal():
    showoff.config(text=showoff.cget("text") + ".")

def intheflesh():
    webbrowser.open("https://www.youtube.com/watch?v=RuJ45E5IxXw")
    
ded()

showoff=Label(text="")
showoff.place(x=100, y=300)

on=Button(text="ON/C", command=on)
on.place(x=10, y=10)

off=Button(text="OFF", command=off)
off.place(x=110, y=10)

a=Button(text="1", command=un)
a.place(x=10, y=60)

b=Button(text="2", command=dos)
b.place(x=110, y=60)

c=Button(text="3", command=tres)
c.place(x=210, y=60)

d=Button(text="4", command=quad)
d.place(x=10, y=110)

e=Button(text="5", command=sink)
e.place(x=110, y=110)

f=Button(text="6", command=six)
f.place(x=210, y=110)

g=Button(text="7", command=sept)
g.place(x=10, y=160)

h=Button(text="8", command=huit)
h.place(x=110, y=160)

i=Button(text="9", command=neuf)
i.place(x=210, y=160)

j=Button(text="0", command=nda)
j.place(x=110, y=210)

plus=Button(text="+", command=add)
plus.place(x=260, y=60)

sub=Button(text="-", command=sub)
sub.place(x=260, y=110)

div=Button(text="/", command=div)
div.place(x=260, y=160)

times=Button(text="x", command=times)
times.place(x=260, y=210)

equal=Button(text="=", command=equal)
equal.place(x=260, y=10)

dec=Button(text=".", command= decimal)
dec.place(x=10, y=210)

music=Button(text="Music", command=intheflesh)
music.place(x=210, y=210)



#daniel helped me out quite a bit
