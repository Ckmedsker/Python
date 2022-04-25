from tkinter import *
from tkinter.messagebox import showinfo

UI = Tk()
UI.title("Echo")


def reply(name):
    showinfo(title="Reply", message = "Hello %s!" % name)


Label(UI, text="Enter your name:").pack(side=TOP)

main_entry = Entry(UI)
main_entry.bind("<Return>", (lambda event: reply(main_entry.get())))
main_entry.pack(side=TOP)

btn = Button(UI,text="Submit", command=(lambda: reply(main_entry.get())))
btn.pack(side=LEFT)

UI.mainloop()