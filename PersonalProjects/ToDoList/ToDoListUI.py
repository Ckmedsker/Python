from tkinter import *
from os.path import exists

BACKG = "skyblue"
FOREG = "white"
FONTC = "black"
WINDOW = "To Do List"
TITLE = "To Do List:"

mainUI = Tk()
mainUI.title(WINDOW)
mainUI.configure(bg=BACKG)
mainUI.geometry("840x600")
mainUI.update_idletasks()
itemsLabel = Label(mainUI)
numbLabel = Label(mainUI)

def labelMaker():
    itemsList = []
    numbList = []
    if exists('Labels.txt'):
        pass
    else:
        open("Labels.txt", "w")
    with open("Labels.txt", "r") as label:
        for i,line in enumerate(label):
            if i < 9:
                s = (f"{i + 1}       \n")
            else:
                s = (f"{i + 1}     \n")
            itemsList.append(f"{line}")
            numbList.append(f"{s}")
        global itemsLabel, numbLabel
        itemsLabel.destroy()
        numbLabel.destroy()
        numbLabel = Label(mainUI, text=(''.join(numbList)), bg=BACKG, fg=FONTC, font="none 16 bold")
        numbLabel.place(relx=0.05, rely=0.15)
        itemsLabel = Label(mainUI, text=(''.join(itemsList)), bg=BACKG, fg=FONTC, font="none 16 bold", justify="left")
        itemsLabel.place(relx=0.1, rely=0.15)
        label.close()


def editToDoList(temp):
    if entry.get() == "" or len(entry.get()) >= 180:
        pass
    elif temp == "add":
        text = entry.get()
        entry.delete(0, END)
        with open("Labels.txt", "r+") as label:
            lines = len(label.readlines())
            if lines <= 27:
                label.write(f"{text}\n")
            else:
                pass
        label.close()
        labelMaker()
        mainUI.update_idletasks()
    elif temp == "remove":
        numb = int(entry.get())
        numb -= 1
        entry.delete(0, END)
        with open("Labels.txt","r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if lines[numb] not in line:
                    file.write(line)
            file.truncate()
            file.close
        labelMaker()


toDoLabel = Label (mainUI,text=TITLE, bg=BACKG, fg=FONTC, font="none 24 bold")
toDoLabel.place(relx=0.5, rely=0.05, anchor=N)

addItem = Button (mainUI, text="Add Item", width=16, height=2, command=lambda:editToDoList("add"))
addItem.place(relx=0.4, rely=0.95, anchor=S)

removeItem = Button (mainUI, text="Remove Item", width=16, height=2, command=lambda:editToDoList("remove"))
removeItem.place(relx=0.6, rely=0.95, anchor=S)

entry = Entry(mainUI)
entry.place(relx=0.5, rely=0.85, anchor=S)


labelMaker()
mainUI.mainloop()