from tkinter import *
windo=Tk()
windo.geometry("400x600")
windo.title("Calculator")
windo.configure(background="#5b7577")
display1=[]
display2=[]
equle1=""
switch=""
finished=0

print("ignore the errors it still works")
def math():
    placeholderint1 = ''.join(display1)
    placeholder1=float(placeholderint1)
        
def math2():
    placeholderint1 = ''.join(display1)
    placeholder1=float(placeholderint1)
    placeholderint2 = ''.join(display2)
    placeholder2=float(placeholderint2)
    
def clear():
    nul=""
    display.config(text=nul)
    nullist=[]
    display1=nullist
    global display1
    global display2
    global equle1
    global switch
    display1=[]
    display2=[]
    equle1=""
    switch=""
    
def buttonequle():
    equle="="
    global equle1
    equle1="="
    placeholderint1 = ''.join(display1)
    placeholder1=float(placeholderint1)
    placeholderint2 = ''.join(display2)
    if  switch!="":
        placeholder2=float(placeholderint2)
    global finished
    finished=1
    if switch=="+":
        product=float(placeholder1 + placeholder2)
    elif switch=="-":
        product=float(placeholder1 - placeholder2)
    elif switch=="*":
        product=float(placeholder1 * placeholder2)
    elif switch=="/":
        product=float(placeholder1 / placeholder2)
 #   elif switch=="":
#        product=float(placeholder1*placeholder1)
        
    nul=""
    display.config(text=nul)
    nullist=[]
    display1=nullist
    global display1
    global display2
    global equle1
    global switch
    display1=[]
    display2=[]
    equle1=""
    switch=""
    display1=[str(product)]
    placeholder1=product
    display.config(text=str(product))   
def buttonplus():
    plus="+"
    global switch
    if switch=="":
        switch="+"
        display.config(text=display.cget("text")+plus)
        math()
def buttonsubtraction():
    subtraction="-"
    global switch
    if switch=="":
        switch="-"
        display.config(text=display.cget("text")+subtraction)
        math()
def buttonmultpilcation():
    multpilcation="*"
    global switch
    if switch=="":
        switch="*"
        display.config(text=display.cget("text")+multpilcation)
        math()
def buttondevide():
    devide="/"
    global switch
    if switch=="":
        switch="/"
        display.config(text=display.cget("text")+devide)
        math()
#makes all the number buttons work
def button0():
    Zero="0"
    if finished==1 and switch=="":
        display.config(text="")
        global display1
        display1=[]
        global finished
        finished=0
    if switch=="" and finished==0:
        display.config(text=display.cget("text")+Zero)
        display1.append("0")
        math()
    else:
        display.config(text=display.cget("text")+Zero)
        display2.append("0")
        math
def button1():
    One="1"
    if finished==1 and switch=="":
        display.config(text="")
        global display1
        display1=[]
        global finished
        finished=0
    if switch=="" and finished==0:
        display.config(text=display.cget("text")+One)
        display1.append("1")
        math()
    else:
        display.config(text=display.cget("text")+One)
        display2.append("1")
        math2()
def button2():
    Two="2"
    if finished==1 and switch=="": 
        display.config(text="")
        global display1
        display1=[]
        global finished
        finished=0
    if switch=="" and finished==0:
        display.config(text=display.cget("text")+Two)
        display1.append("2")
        math()
    else:
        display.config(text=display.cget("text")+Two)
        display2.append("2")
        math2()
def button3():
    Three="3"
    if finished==1 and switch=="":
        display.config(text="")
        global display1
        display1=[]
        global finished
        finished=0
    if switch=="" and finished==0:
        display.config(text=display.cget("text")+Three)
        display1.append("3")
        math()
    else:
        display.config(text=display.cget("text")+Three)
        display2.append("3")
        math2()
def button4():
    Four="4"
    if finished==1 and switch=="":
        display.config(text="")
        global display1
        display1=[]
        global finished
        finished=0
    if switch=="" and finished==0:
        display.config(text=display.cget("text")+Four)
        display1.append("4")
        math()
    else:
        display.config(text=display.cget("text")+Four)
        display2.append("4")
        math2()
        
def button5():
    Five="5"
    if finished==1 and switch=="":
        display.config(text="")
        global display1
        display1=[]
        global finished
        finished=0
    if switch=="" and finished==0:
        display.config(text=display.cget("text")+Five)
        display1.append("5")
        math()
    else:
        display.config(text=display.cget("text")+Five)
        display2.append("5")
        math2()
        
def button6():
    Six="6"
    if finished==1 and switch=="":
        display.config(text="")
        global display1
        display1=[]
        global finished
        finished=0
    if switch=="" and finished==0:
        display.config(text=display.cget("text")+Six)
        display1.append("6")
        math()
    else:
        display.config(text=display.cget("text")+Six)
        display2.append("6")
        math2()
        
def button7():
    seven="7"
    if finished==1 and switch=="":
        display.config(text="")
        global display1
        display1=[]
        global finished
        finished=0
    if switch=="" and finished==0:
        display.config(text=display.cget("text")+seven)
        display1.append("7")
        math()
    else:
        display.config(text=display.cget("text")+seven)
        display2.append("7")
        math2()
        
def button8():
    Eight="8"
    if finished==1 and switch=="":
        display.config(text="")
        global display1
        display1=[]
        global finished
        finished=0
    if switch=="" and finished==0:
        display.config(text=display.cget("text")+Eight)
        display1.append("8")
        math()
    else:
        display.config(text=display.cget("text")+Eight)
        display2.append("8")
        math2()
        
def button9():
    Nine="9"
    if finished==1 and switch=="":
        display.config(text="")
        global display1
        display1=[]
        global finished
        finished=0
    if switch=="" and finished==0:
        display.config(text=display.cget("text")+Nine)
        display1.append("9")
        math()
    else:
        display.config(text=display.cget("text")+Nine)
        display2.append("9")
        math2()
        
def squarebutton():
    square="^2"
    if finished==1:
        display.config(text="")
        global display1
        display1=[]
        global finished
        finished=0
    if switch=="":
        display.config(text=display.cget("text")+square)
        display1.append(".")
        math()
    else:
        display.config(text=display.cget("text")+square)
        display2.append("^2")
        math2()
    buttonequle()
    
def buttondot():
    dot="."
    if finished==1:
        display.config(text="")
        global display1
        display1=[]
        global finished
        finished=0
    if switch=="":
        display.config(text=display.cget("text")+dot)
        display1.append(".")
        math()
    else:
        display.config(text=display.cget("text")+dot)
        display2.append(".")
        math2()
        
def negbutton():
    neg="-"
    placeholderint1 = ''.join(display1)
    placeholder1=float(placeholderint1)
    if switch=="":
            display.config(text="-"+str(''.join(display1))+switch+str(''.join(display2)))
            display1.insert(0,neg)
            math()
    else:
        display.config(text=str(''.join(display1))+switch+"-"+str(''.join(display2)))
        display2.insert(0,neg)
        math()

        
#places all the buttons
#display=Label(text="The Great Base 10 Calculator", fg="#1c1b1a",bg="#9ea5af",height=2,width=30)
#display.place(x=70, y=20)
display=Label(text="", fg="#1c1b1a",bg="#c1bcb2",height=3,width=30)
display.place(x=70, y=75)
Onebutton= Button(text = "1", command=button1, highlightbackground="#5b7577")
Onebutton.place(x=175/2, y=170)
Twobutton= Button(text = "2", command =button2,highlightbackground="#5b7577")
Twobutton.place(x=175, y=170)
Threebutton= Button(text = "3", command =button3,highlightbackground="#5b7577")
Threebutton.place(x=270, y=170)
Fourbutton= Button(text = "4", command =button4,highlightbackground="#5b7577")
Fourbutton.place(x=175/2, y=260)
Fivebutton= Button(text = "5", command =button5,highlightbackground="#5b7577")
Fivebutton.place(x=175, y=260)
Sixbutton=Button(text = "6", command =button6,highlightbackground="#5b7577")
Sixbutton.place(x=270, y=260)
sevenbutton=Button(text = "7", command =button7,highlightbackground="#5b7577")
sevenbutton.place(x=175/2, y=340)
Eightbutton=Button(text = "8", command =button8,highlightbackground="#5b7577")
Eightbutton.place(x=175, y=340)
Ninebutton=Button(text = "9", command =button9,highlightbackground="#5b7577")
Ninebutton.place(x=270, y=340)
Plusebutton=Button(text = "+", command =buttonplus,highlightbackground="#5b7577")
Plusebutton.place(x=365, y=170)
EquleButton=Button(text="=",command=buttonequle,highlightbackground="#5b7577")
EquleButton.place(x=270 ,y=415)
subtractionButton=Button(text="-",command=buttonsubtraction,highlightbackground="#5b7577")
subtractionButton.place(x=365 ,y=260)
multpilcationButton=Button(text="*",command=buttonmultpilcation,highlightbackground="#5b7577")
multpilcationButton.place(x=365 ,y=340)
devideButton=Button(text="/",command=buttondevide,highlightbackground="#5b7577")
devideButton.place(x=365 ,y=415)
Zerobutton=Button(text="0",command=button0,highlightbackground="#5b7577")
Zerobutton.place(x=175/2,y=415)
ClearButton=Button(text="Clear",command=clear,highlightbackground="#5b7577")
ClearButton.place(x=165 ,y=415)
ButtonNeg=Button(text="Neg",command=negbutton,highlightbackground="#5b7577")
ButtonNeg.place(x=167,y=485)
dotbutton=Button(text=".",command=buttondot,highlightbackground="#5b7577")
dotbutton.place(x=175/2 ,y=485)
#dotbutton=Button(text="Square",command=squarebutton)
#dotbutton.place(x=250 ,y=485)
