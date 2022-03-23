from tkinter import *


import random
import time

count = 0

window = Tk()
window.geometry("1500x700")
window.title("Hey Saber")
window.configure(background = "black")

for _ in range(34):
    for j in range(90):
        Label (window, text = "A", bg="black", fg=(f"{r}{g}{b}"), font = "none 12 bold") .grid(row=count, column=j)
    count += 1


window.mainloop()
