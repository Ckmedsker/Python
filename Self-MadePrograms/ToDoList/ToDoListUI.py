from fileinput import close
from tkinter import *

BACKG = "green"
FOREG = "white"

def close_window():
    mainUI.destroy()
    exit()
def labelMaker():
    labelArray = []
    labels = []
    with open("Labels.txt", "r") as label:
        for i,line in enumerate(label):
            print(i)
            labels.append(line.strip("\n"))
            labelArray.append(Label (mainUI, text=labels[i], bg=BACKG, fg="black", font="none 12 bold"))
            labelArray[i].place(relx=0.1, rely=(0.1 + 0.05 * (i+1)))
                            #vertical placement|distance between values|multiplier


mainUI = Tk()
mainUI.title("To Do List:")
mainUI.configure(bg=BACKG)
mainUI.geometry("840x600")
mainUI.update()
labelMaker()

ToDoLabel = Label (mainUI,text="To Do List", bg=BACKG, fg="black", font="none 24 bold")
ToDoLabel.place(relx=0.5, rely=0.05, anchor=N)
EXIT = Button (mainUI, text="EXIT", width=16, height=2, command=close_window)
EXIT.place(relx=0.5, rely=0.95, anchor=S)

mainUI.mainloop()