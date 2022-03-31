from tkinter import *
from os.path import exists

from numpy import delete

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
recent_searches = []
error_label = Button(UI)
error = ""
if exists(FILE):
    pass
else:
    open(FILE, "w")

# Making the visuals for the Main Page
def main_page():
    def search_func():
        global error_label
        error_label.place_forget()
        text = entry_box.get().lower()
        entry_box.delete(0, END)
        if text != "":
            text = list(text)
            text[0] = text[0].capitalize()
            text = ''.join(text)
        with open(FILE, "r") as dict:
            for line in lines:
                if line.strip("\n") == text:
                    destroy_main(widgets, recent_searches)
                    word_page(text)
            dict.close() 
        if text == "" or (f"{text}\n") not in lines:
            error = "Please enter a word in the dictionary!"
        else:
            error = ""
            
        error_label = Label(UI, text=error, bg=BACKG, fg=FONTC, font="none 12 bold")
        error_label.place(relx=0.5, rely=0.79, anchor=S)
    def add_word():
        text = entry_box.get().lower()
        text = list(text)
        text[0] = text[0].capitalize()
        entry_box.delete(0, END)
        dict_items.delete(0, END)
        with open(FILE, "r") as dict:
            lines = dict.readlines()
            lines.append(f"{''.join(text)}\n")
            lines.sort()
            dict.close()
        with open(FILE, "w+") as dict:
            for line in lines:
                dict.write(line)
                dict_items.insert(END, line.strip("\n"))
            dict.close()
    def destroy_main(widgets, recent_searches):
        for i, j in zip(widgets, recent_searches):
            i.destroy()
            j.destroy()
        recent_searches.clear()
        

    dict_label = Label(UI,text="Dictionary", bg=BACKG, fg=FONTC, font="none 24 bold")
    dict_label.place(relx=0.5, rely=0.01, anchor=N)

    scrollbar = Scrollbar(UI, orient="vertical")
    
    dict_items = Listbox(UI, bg=BBACKG, fg=FONTC, width=25, height=14, font="none 20 bold", yscrollcommand=scrollbar.set)
    dict_items.place(relx=0.5, rely=0.08, anchor=N)

    info_label = Label(UI,text="Type in the entry box to search or add definitions!", bg=BACKG, fg=FONTC, font="none 12 bold")
    info_label.place(relx=0.5, rely=0.68, anchor=S)

    entry_box = Entry(UI, bg=BBACKG, fg=FONTC, width=20, font="none 20 bold")
    entry_box.place(relx=0.5, rely=0.76, anchor=S)

    search = Button(UI, text="Search", bg=BBACKG, fg=FONTC, width=24, height=4, font="none 9 bold", command=search_func)
    search.place(relx=0.4, rely=0.91, anchor=S)

    add_word_button = Button(UI, text="Add Word!", bg=BBACKG, fg=FONTC, width=24, height=4, font="none 9 bold", command=add_word)
    add_word_button.place(relx=0.6, rely=0.91, anchor=S)
    
    random = Button(UI, text="Go To Random Entry!", bg=BBACKG, fg=FONTC, width=32, height=4, font="none 9 bold")
    random.place(relx=0.85, rely=0.41, anchor=S)

    recent_label = Label(UI, text="These are the 10 most recent searches!", bg= BACKG, fg=FONTC, font="none 12 bold")
    recent_label.place(relx=0.155, rely=0.23, anchor=S)

    # For the 10 most recent searches
    for i in range(0,10):
        if i <= 4:
            x = 0.08
            y = 0
        else:
            x = 0.23
            y = 0.25
        recent_searches.append(Button(UI, text=(f"Button: {i + 1}"), bg=BBACKG, fg=FONTC, width=16, font="none 9 bold"))
        recent_searches[i].place(relx=x, rely=(i / 20) + 0.28 - y, anchor=S)
    
    with open(FILE, "r") as dict:
        lines = dict.readlines()
        for line in lines:
            dict_items.insert(END, line.strip("\n"))
        dict.close()


#   test = Label (UI, width=10, height=9, bg="green", font="none 9 bold")
#   test.place(relx=0.25, rely=0.249, anchor=S)
#   test1 = Label (UI, width=10, height=9, bg="green", font="none 9 bold")
#   test1.place(relx=0.25, rely=0.647, anchor=S)
#   setting a list of all the widgets to delete all widgets
    widgets = [dict_label, scrollbar, dict_items, info_label, entry_box, error_label,
    search, add_word_button, random, recent_label]

# Setting up specific pages for each individual word
def word_page(word):
    def destroy_entry():
        print("deleted")
    def destroy_word(widgets):
        for i in widgets:
            i.destroy()
        main_page()
    dict_label = Label(UI,text=word, bg=BACKG, fg=FONTC, font="none 24 bold")
    dict_label.place(relx=0.5, rely=0.01, anchor=N)

    return_button = Button(UI, text="<- Back to Main Page", bg=BBACKG, fg=FONTC, width=24, height=4, font="none 9 bold", command=lambda:destroy_word(widgets))
    return_button.place(relx=0.4, rely=0.91, anchor=S)

    delete_entry = Button(UI, text="Delete Word", bg=BBACKG, fg=FONTC, width=24, height=4, font="none 9 bold", command=destroy_entry)
    delete_entry.place(relx=0.6, rely=0.91, anchor=S)

    widgets = [dict_label, return_button, delete_entry]

main_page()
UI.mainloop()