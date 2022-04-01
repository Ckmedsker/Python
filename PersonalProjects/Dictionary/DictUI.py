from tkinter import *
from os.path import exists
import random


# Static Variables
BACKG = "black"
BBACKG = "white"
FOREG = "red"
FONTC = "brown"
FILE = "dictionary.txt"
FILE1 = "search_history.txt"

# UI Initialization
UI = Tk()
UI.title("Dictionary")
UI.configure(bg=BACKG)
UI.geometry("1000x825")
UI.minsize(1000, 825)

# Initialization
recent_searches_list = []
error_label = Button(UI)
error = ""
if not exists(FILE):
    open(FILE, "w")
if not exists(FILE1):
    open(FILE1, "w")

# Making the visuals for the Main Page
def main_page():
    def search_func(input):
        global error_label, error
        error_label.destroy()
        text = entry_box.get().lower()
        if input != "":
            text = input.strip("\n").lower()
        entry_box.delete(0, END)
        lines = open(FILE, "r").readlines()
        format_list = []
        for line in lines:
            format_list.append(line.strip("\n").lower())
        if text == "" or text not in format_list:
            error = "Please enter a word in the dictionary!"
            error_label = Label(UI, text=error, bg=BACKG,
                                fg=FONTC, font="none 12 bold")
            error_label.place(relx=0.5, rely=0.79, anchor=S)
        else:
            text = list(text)
            text[0] = text[0].capitalize()
            text = ''.join(text)
            for line in lines:
                if line.strip("\n") == text:
                    destroy_main(widgets, recent_searches_list)
                    word_page(text)
            in_dict = False
            with open(FILE1, "r") as dict:
                lines = dict.readlines()
                for line in lines:
                    if text.lower() == line.strip("\n").lower():
                        in_dict = True
                if in_dict != True:
                    lines.insert(0, f"{text}\n")
                else:
                    for j, line in enumerate(lines):
                        if line.strip("\n") == text:
                            lines.insert(0, line)
                            lines.pop(j+1)
            # Matching to dict_items listbox to the text file
            if input == "":
                with open(FILE1, "w+") as dict:
                    for line in lines:
                        dict.write(line)


    def add_word():
        global error_label, error
        error_label.destroy()
        text = entry_box.get().lower()
        if text != "":
            text = list(text)
            text[0] = text[0].capitalize()
            text = ''.join(text)
            entry_box.delete(0, END)
            dict_items.delete(0, END)
            in_dict = False
            with open(FILE, "r") as dict:
                lines = dict.readlines()
                for line in lines:
                    if text.lower() == line.strip("\n").lower():
                        error = "This word is already in the dictionary!"
                        in_dict = True
                if in_dict != True:
                    lines.append(f"{text}\n")
                    lines.sort()
            # Matching to dict_items listbox to the text file
            with open(FILE, "w+") as dict:
                for line in lines:
                    dict.write(line)
                    dict_items.insert(END, line.strip("\n"))
        else:
            error = "Please enter a word!"
        if error != "":
            error_label = Label(UI, text=error, bg=BACKG,
                                fg=FONTC, font="none 12 bold")
            error_label.place(relx=0.5, rely=0.79, anchor=S)

    def destroy_main(widgets, recent_searches):
        for i, j in zip(widgets, recent_searches):
            i.destroy()
            j.destroy()
        recent_searches.clear()

    def random_entry():
        temp = open(FILE, "r").readlines()
        rand = random.randint(0, (len(temp) - 1))
        search_func(temp[rand])

    dict_label = Label(UI, text="Dictionary", bg=BACKG,
                       fg=FONTC, font="none 24 bold")
    dict_label.place(relx=0.5, rely=0.01, anchor=N)

    scrollbar = Scrollbar(UI, orient="vertical")

    dict_items = Listbox(UI, bg=BBACKG, fg=FONTC, width=25, height=14,
                         font="none 20 bold", highlightbackground=BACKG, yscrollcommand=scrollbar.set)
    dict_items.place(relx=0.5, rely=0.08, anchor=N)

    info_label = Label(UI, text="Type in the entry box to search or add definitions!",
                       bg=BACKG, fg=FONTC, font="none 12 bold")
    info_label.place(relx=0.5, rely=0.68, anchor=S)

    entry_box = Entry(UI, bg=BBACKG, fg=FONTC, width=20, font="none 20 bold")
    entry_box.place(relx=0.5, rely=0.76, anchor=S)

    search = Button(UI, text="Search", bg=BBACKG, fg=FONTC,
                    width=24, height=4, font="none 8 bold", command=lambda: search_func(""))
    search.place(relx=0.4, rely=0.91, anchor=S)

    add_word_button = Button(UI, text="Add Word!", bg=BBACKG, fg=FONTC,
                             width=24, height=4, font="none 8 bold", command=add_word)
    add_word_button.place(relx=0.6, rely=0.91, anchor=S)

    random_button = Button(UI, text="Go To Random Entry!", bg=BBACKG,
                           fg=FONTC, width=32, height=4, font="none 8 bold", command=random_entry)
    random_button.place(relx=0.85, rely=0.41, anchor=S)

    recent_label = Label(UI, text="These are the 10 most recent searches!",
                         bg=BACKG, fg=FONTC, font="none 12 bold")
    recent_label.place(relx=0.155, rely=0.23, anchor=S)

    # For the 10 most recent searches buttons
    temp = open(FILE1, "r").readlines()
    if len(temp) <= 10:
        for i in range(0, 11 - len(temp)):
            temp.append("Less than \n10 Searches!")
    for i in range(0, 10):
        if i <= 4:
            x = 0.08
            y = 0
        else:
            x = 0.23
            y = 0.25
        recent_searches_list.append(Label(UI, text=(
            f"{i + 1}: {temp[i]}"), bg=BACKG, fg=FONTC, width=17, font="none 10 bold"))
        recent_searches_list[i].place(
            relx=x, rely=(i / 20) + 0.28 - y, anchor=S)

    with open(FILE, "r") as dict:
        lines = dict.readlines()
        for line in lines:
            dict_items.insert(END, line.strip("\n"))

#   setting a list of all the widgets to delete all widgets
    widgets = [dict_label, scrollbar, dict_items, info_label, entry_box, error_label,
               search, add_word_button, random_button, recent_label]

# Setting up specific pages for each individual word


def word_page(word):
    def destroy_entry(word):
        lines = open(FILE, "r").readlines()
        with open(FILE, "w") as fp:
            for line in lines:
                if line.strip("\n") != word:
                    fp.write(line)
        lines = open(FILE1, "r").readlines()
        with open(FILE1, "w") as fp:
            for line in lines:
                if line.strip("\n") != word:
                    fp.write(line)
        destroy_word(widgets1)

    def destroy_word(widgets1):
        for i in widgets1:
            i.destroy()
        main_page()
    dict_label = Label(UI, text=word, bg=BACKG, fg=FONTC, font="none 24 bold")
    dict_label.place(relx=0.5, rely=0.01, anchor=N)

    return_button = Button(UI, text="<- Back to Main Page", bg=BBACKG, fg=FONTC,
                           width=24, height=4, font="none 8 bold", command=lambda: destroy_word(widgets1))
    return_button.place(relx=0.4, rely=0.91, anchor=S)

    delete_entry = Button(UI, text="Delete Word", bg=BBACKG, fg=FONTC, width=24,
                          height=4, font="none 8 bold", command=lambda: destroy_entry(word))
    delete_entry.place(relx=0.6, rely=0.91, anchor=S)

    widgets1 = [dict_label, return_button, delete_entry]


main_page()
UI.mainloop()
