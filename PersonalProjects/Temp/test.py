from tkinter import *


# Static Variables
BACKG = "lime"
BBACKG = "cyan"
FOREG = "red"
FONTC = "black"
FILE = "Cybersecurity_Acronyms2.md"

# UI Initialization
UI = Tk()
UI.title("Dictionary")
UI.configure(bg=BACKG)
UI.geometry("1000x825")
UI.minsize(1000, 825)


def temp():
    print("hehe")


def temp_acronym_entry(e):
    acronym_entry.delete(0, "end")
def add_temp_acronym_entry(e):
    acronym_entry.insert(0, "Enter an acronym!")
def temp_word_entry(e):
    word_entry.delete(0, "end")
def add_temp_word_entry(e):
    word_entry.insert(0, "Enter a definition!")
def change_look():
    acronyms.see(400)


# Main Page
main_label = Label(UI, text="Acronyms", bg=BACKG,
                   fg=FONTC, font="none 35 bold")
main_label.place(relx=0.5, rely=0.01, anchor=N)

scrollbar = Scrollbar(UI, orient="vertical")

acronyms = Listbox(UI, bg=BBACKG, fg=FONTC, width=95, height=23,
                   font="none 12 bold", highlightbackground=BACKG, yscrollcommand=scrollbar.set)
acronyms.place(relx=0.5, rely=0.08, anchor=N)

info_label = Label(UI, text="Type in an acronym to search it, or add a new acronym.",
                   bg=BACKG, fg=FONTC, font="none 12 bold")
info_label.place(relx=0.5, rely=0.68, anchor=S)

acronym_entry = Entry(UI, bg=BBACKG, fg=FONTC, width=20, font="none 20 bold")
acronym_entry.place(relx=0.5, rely=0.73, anchor=S)
acronym_entry.insert(0, "Enter an acronym!")
acronym_entry.bind("<FocusIn>", temp_acronym_entry)
acronym_entry.bind("<FocusOut>", add_temp_acronym_entry)

word_entry = Entry(UI, bg=BBACKG, fg=FONTC, width=20, font="none 20 bold")
word_entry.place(relx=0.5, rely=0.78, anchor=S)
word_entry.insert(0, "Enter a definition!")
word_entry.bind("<FocusIn>", temp_word_entry)
word_entry.bind("<FocusOut>", add_temp_word_entry)


search = Button(UI, text="Search", bg=BBACKG, fg=FONTC,
                width=24, height=4, font="none 8 bold", command=change_look)
search.place(relx=0.4, rely=0.91, anchor=S)

add_word_button = Button(UI, text="Add Acronym", bg=BBACKG, fg=FONTC,
                         width=24, height=4, font="none 8 bold", command=temp)
add_word_button.place(relx=0.6, rely=0.91, anchor=S)


with open(FILE, "r") as items:
    lines = items.readlines()
    for line in lines:
        acronyms.insert(END, line.strip("\n"))
UI.mainloop()
