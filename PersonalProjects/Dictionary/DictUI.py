from tkinter import *
from os.path import exists
import random
import requests


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
definition_labels = []
error_label = Button(UI)
error = ""
error_bool = False
widgets = []
widgets1 = []
def file_checker():
    if not exists(FILE):
        open(FILE, "w")
    if not exists(FILE1):
        open(FILE1, "w")
file_checker()

# Making the visuals for the Main Page
def main_page():
    def search_func(input):
        global error_label, error, error_bool
        file_checker()
        error_label.destroy()
        text = entry_box.get().lower()
        if text == "" and dict_items.curselection() != ():
            temp = int(list(dict_items.curselection())[0])
            with open(FILE, "r") as dict:
                items = dict.readlines()
                text = items[temp].lower().strip("\n")
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
            error_bool = False
            with open(FILE1, "r") as dict:
                lines = dict.readlines()
                for line in lines:
                    if text.lower() == line.strip("\n").lower():
                        error_bool = True
                if error_bool == False:
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
            dict_api(text, True)

    def add_word():
        global error_label, error, error_bool
        file_checker()
        error_label.destroy()
        text = entry_box.get().lower()
        if text != "":
            dict_api(text, False)
            text = list(text)
            text[0] = text[0].capitalize()
            text = ''.join(text)
            entry_box.delete(0, END)
            dict_items.delete(0, END)
            with open(FILE, "r") as dict:
                lines = dict.readlines()
                for line in lines:
                    if text.lower() == line.strip("\n").lower():
                        error = "This word is already in the dictionary!"
                        error_bool = True
                if error_bool == False:
                    lines.append(f"{text}\n")
                    lines.sort()
            # Matching to dict_items listbox to the text file
            with open(FILE, "w+") as dict:
                for line in lines:
                    dict.write(line)
                    dict_items.insert(END, line.strip("\n"))
            
        else:
            error = "Please enter a word!"
        error_label = Label(UI, text=error, bg=BACKG,
                            fg=FONTC, font="none 12 bold")
        error_label.place(relx=0.5, rely=0.79, anchor=S)

    def dict_api(word, check):
        global definition_labels, error, error_bool
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        definition = response.json()
        definitions = []
        if len(definition) == 3:
            error = "This word has no dictionary definitions!"
            error_bool = True
        else:
            if len(definition[0]['meanings'][0]['definitions']) < 5:
                numb = len(definition[0]['meanings'][0]['definitions'])
            else:
                numb = 5
            for i in range(0, numb):
                definitions.append(definition[0]['meanings'][0]['definitions'][i]['definition'])
            # Make up to 5 labels for definitions
            if check == True:
                for j in range(0, len(definitions)):
                    definition_labels.append(Label(UI, text=definitions[j],
                                        bg=BACKG, fg=FONTC, justify="left", font="none 12 bold"))
                    definition_labels[j].place(relx=0.5, rely=0.23 + (j / 10), anchor=CENTER)
            error = ""
            error_bool = False
        return error_bool

    def destroy_main(widgets, recent_searches):
        for i, j in zip(widgets, recent_searches):
            i.destroy()
            j.destroy()
        recent_searches.clear()

    def random_entry():
        dict = open(FILE, "r").readlines()
        rand = random.randint(0, (len(dict) - 1))
        search_func(dict[rand])

    dict_label = Label(UI, text="Dictionary", bg=BACKG,
                       fg=FONTC, font="none 35 bold")
    dict_label.place(relx=0.5, rely=0.01, anchor=N)

    scrollbar = Scrollbar(UI, orient="vertical")

    dict_items = Listbox(UI, bg=BBACKG, fg=FONTC, width=25, height=14,
                         font="none 20 bold", highlightbackground=BACKG, yscrollcommand=scrollbar.set)
    dict_items.place(relx=0.5, rely=0.08, anchor=N)

    info_label = Label(UI, text="Type in the entry box/select an item to search or add words!",
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

    recent_label = Label(UI, text="these are the 10 most recent searches!",
                         bg=BACKG, fg=FONTC, font="none 12 bold")
    recent_label.place(relx=0.155, rely=0.23, anchor=S)

    # For the 10 most recent searches buttons
    dict_list = open(FILE1, "r").readlines()
    if len(dict_list) <= 10:
        for i in range(0, 11 - len(dict_list)):
            dict_list.append("Less than \n10 Searches!")
    for i in range(0, 10):
        if i <= 4:
            x = 0.08
            y = 0
        else:
            x = 0.23
            y = 0.25
        recent_searches_list.append(Label(UI, text=(
            f"{i + 1}: {dict_list[i]}"), bg=BACKG, fg=FONTC, width=17, font="none 10 bold"))
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
        file_checker()
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
        file_checker()
        for i in widgets1:
            i.destroy()
        for j in definition_labels:
            j.destroy()
        definition_labels.clear()
        main_page()


    word_label = Label(UI, text=word, bg=BACKG, fg=FONTC, font="none 35 bold")
    word_label.place(relx=0.5, rely=0.01, anchor=N)

    info_label = Label(UI, text="These are the top 5 definitions!", bg=BACKG, fg=FONTC, font="none 20 bold")
    info_label.place(relx=0.5, rely=0.08, anchor=N)

    return_button = Button(UI, text="<- Back to Main Page", bg=BBACKG, fg=FONTC,
                           width=24, height=4, font="none 8 bold", command=lambda: destroy_word(widgets1))
    return_button.place(relx=0.4, rely=0.91, anchor=S)

    delete_entry = Button(UI, text="Delete Word", bg=BBACKG, fg=FONTC, width=24,
                          height=4, font="none 8 bold", command=lambda: destroy_entry(word))
    delete_entry.place(relx=0.6, rely=0.91, anchor=S)

    widgets1 = [word_label, info_label, return_button, delete_entry]


main_page()
UI.mainloop()
