import tkinter as tk
from tkinter.ttk import LabeledScale


BACKG = "skyblue"
FOREG = "white"

mainUI = tk.Tk()
mainUI.title("To Do List:")
mainUI.configure(bg=BACKG)
mainUI.geometry("840x600")
mainUI.update_idletasks()
oneLabel = tk.Label(mainUI)


def labelMaker():
    labelArray = []
    labels = []
    num = []
    with open("Labels.txt", "r") as label:
        for i,line in enumerate(label):
            #oneLabel = tk.Label (mainUI, text=("filler"), bg="green", fg="black", font="none 12 bold")
            global oneLabel
            oneLabel.destroy()
            labels.append(line.strip("\n"))
            #labelArray.append(tk.Label (mainUI, text=labels[i], bg="green", fg="black", font="none 12 bold"))
            #labelArray[i].place(relx=0.1, rely=(0.1 + 0.05 * (i+1)))
                            #vertical placement|distance between values|multiplier
            #num.append(tk.Label (mainUI, text=i+1, bg="green", fg="black", font="none 12 bold"))
            #num[i].place(relx=0.05, rely=(0.1 + 0.05 * (i+1)))
        oneLabel = tk.Label (mainUI, text=(f"{i}     {labels[i]}\n"), bg="green", fg="black", font="none 12 bold")
        oneLabel.place(relx=0.05, rely=(0.1 + 0.05 * (i+1)))
        label.close()


def editToDoList(temp):
    if entry.get() == "" or len(entry.get()) >= 40:
        pass
    elif temp == "add":
        text = entry.get()
        entry.delete(0, tk.END)
        addItem = open("Labels.txt", "a")
        addItem.write(f"{text}\n")
        addItem.close()
        labelMaker()
        mainUI.update_idletasks()
    elif temp == "remove":
        text = entry.get()
        entry.delete(0, tk.END)
        #print("balls")
        #toDoLabel['state'] = tk.DISABLED
        #oneLabel.destroy()
        labelMaker()
        mainUI.update_idletasks()


toDoLabel = tk.Label (mainUI,text="To Do List", bg="green", fg="black", font="none 24 bold")
toDoLabel.place(relx=0.5, rely=0.05, anchor=tk.N)

addItem = tk.Button (mainUI, text="Add Item", width=16, height=2, command=lambda:editToDoList("add"))
addItem.place(relx=0.4, rely=0.95, anchor=tk.S)

removeItem = tk.Button (mainUI, text="Remove Item", width=16, height=2, command=lambda:editToDoList("remove"))
removeItem.place(relx=0.6, rely=0.95, anchor=tk.S)

entry = tk.Entry(mainUI)
entry.place(relx=0.5, rely=0.85, anchor=tk.S)

labelMaker()
mainUI.mainloop()