from tkinter import *

class loginfirst():
    def init(self,master):

        self.master=master
        self.master.geometry("400x400")
        self.title("A game with a title to be decided later")

        self.binit1 = Button(self.master, text="Create Account", command=self.makeit)
        self.binit1.place = (x=3, y=1)

        self.binit2 = Button(self.master, text="Login", command=self.useit)
        self.binit2.place = (row=3, column=1)

    def makeit(self):

        win2 = Toplevel(self.master)
        myWIN = Make Account(win2,self)

    def useit(self):
        self.master.destroy()

loginfirst()
