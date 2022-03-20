from tkinter import *

def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        definition = my_compdictorionary[entered_text]
    except:
        definition = "That is not in the dictionary"
    output.insert(END,definition)

def close_window():
    window.destroy()
    exit()
window = Tk()
window.title("My Computer Science Glossary")
window.configure(background="black")

#photo1 = PhotoImage(file="meme13.png")
#image=photo1 V
Label (window, bg="black") .grid(row=0, column=0, sticky=E)

Label (window,text="Enter the word you would like a definition for!: ", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0)

textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2,column=0)

Button(window, text="SUBMIT", width=6, command=click) .grid(row=3, column=0)

Label (window, text="Definition:", bg="black", fg="white", font="none 12 bold") .grid(row=4,column=0)

output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2)

my_compdictorionary = {
    "algorithm": "Step by step instructions to complete a task", "bug": "piece of code that causes a program to fail"
}

Button (window, text="EXIT", width=14, command=close_window) .grid(row=7,column=0)

window.mainloop()