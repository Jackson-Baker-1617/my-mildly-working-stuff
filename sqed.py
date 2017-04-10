from tkinter import *

class HomePage():       #defines the attributes of the home page
    def __init__(self, master):     # init defines what should happen when the home page opens up
                                    #master is the parent window(widget) and the widgets (buttons, labels...) we put in master are the children
                                    #self is a way for each of your commands to reference itself
        
        self.master=master
        self.master.geometry("300x300")
        self.master.title("Home Page")

        self.button1 = Button(self.master, text="Next Page", command=self.nextpage)
        self.button1.grid(row=0, column=0)      #notice we use self. for everything in order to keep it in the parent widget

        self.button2 = Button(self.master, text="QUIT", command=self.done)
        self.button2.grid(row=0, column=1)

    def nextpage(self):     #we need to define what the buttons do just like before, but notice we don't have to put
                               #   this def at the top of the code before the buttons are created.
        win2 = Toplevel(self.master)    #creates a new window that is dependent on the original window
        myWIN = NextPage(win2, self)  #naming the class for the new window as NextPage

    def done(self):
        self.master.destroy()   #when the original window is destroyed, all windows associated with it are destroyed

class NextPage():   #time to define the second window that we called NextPage

    def __init__(self, master, win, ):

        #defining variables I'll use in this window
        self.num1 = DoubleVar()  #DoubleVar() makes the value stored in it a float
        self.num2 = DoubleVar()
        
        self.master=master
        self.master.geometry("500x500")
        self.master.title("Home Page")

        self.label1 = Label(self.master, text = "Enter a number")
        self.label1.grid(row=0, column=0)

        self.label2 = Label(self.master, text = "Enter a second number")
        self.label2.grid(row=1, column=0)

        self.entry1 = Entry(self.master, textvariable=self.num1)
        self.entry1.grid(row=0, column=1)

        self.entry2 = Entry(self.master, textvariable=self.num2)
        self.entry2.grid(row=1, column=1)

        self.button1 = Button(self.master, text="Click here to add", command=self.button1)
        self.button1.grid(row=2, column=0)

        self.button2 = Button(self.master, text="Go Back Home", command=self.back)
        self.button2.grid(row=3, column=0)

    def button1(self):
        number1 = self.num1.get()
        number2 = self.num2.get()
        self.label3 = Label(self.master, text = number1 + number2)
        self.label3.grid(row=2, column=1)

    def back(self):
        self.master.destroy()

def main():
    win = Tk()
    myGUIwelcome = HomePage(win)     #defines the main window as HomePage

   #sets up main as the place to start this program
main()
