from tkinter import *
from os.path import exists

# Static Variables
BACKG = "black"
BBACKG = "white"
FOREG = "red"
FONTC = "brown"
FILE = "dictionary.txt"

# UI Initialization
UI = Tk()
UI.title("Dictionary")
UI.configure(bg=BACKG)
UI.geometry("1000x825")
UI.minsize(1000, 825)

# Initialization
recent_searches = []
if exists(FILE):
    pass
else:
    open(FILE, "w")

# Deals with file
#def file_stuff():
#   if exists(FILE):
#       pass
#   else:
#       open(FILE, "w")
#   with open(FILE, "r") as label:
#       print("temp")
# Making the visuals for the Main Page
def main_page():
    def search_func():
        text = entry_box.get()
        entry_box.delete(0, END)
    def add_word():
        text = entry_box.get()
        entry_box.delete(0, END)
        with open(FILE, "a") as label:
            label.write(f"{text}\n")
            # IDEA to alphabetize list, insert item where it belongs rather than at the end
            dict_items.insert(END, text)
    

    dict_label = Label (UI,text="Dictionary", bg=BACKG, fg=FONTC, font="none 24 bold")
    dict_label.place(relx=0.5, rely=0.01, anchor=N)

    scrollbar = Scrollbar(UI, orient="vertical")
    
    dict_items = Listbox(UI, bg=BBACKG, fg=FONTC, width=60, height=29, yscrollcommand=scrollbar.set)
    dict_items.place(relx=0.5, rely=0.08, anchor=N)

    info_label = Label (UI,text="Type in the entry box to search or add definitions!", bg=BACKG, fg=FONTC, font="none 12 bold")
    info_label.place(relx=0.5, rely=0.68, anchor=S)

    entry_box = Entry(UI, bg=BBACKG, fg=FOREG, width=20, font="none 20 bold")
    entry_box.place(relx=0.5, rely=0.76, anchor=S)

    error_label = Label (UI, text="Enter in a word in the dictionary!", bg=BACKG, fg=FONTC, font="none 12 bold")
    error_label.place(relx=0.5, rely=0.79, anchor=S)

    search = Button (UI, text="Search", bg=BBACKG, fg=FONTC, width=24, height=4, font="none 9 bold", command=lambda:destroy_main(widgets, recent_searches))
    search.place(relx=0.4, rely=0.91, anchor=S)

    add_word_button = Button(UI, text="Add Word!", bg=BBACKG, fg=FONTC, width=24, height=4, font="none 9 bold", command=add_word)
    add_word_button.place(relx=0.6, rely=0.91, anchor=S)
    
    random = Button (UI, text="Go To Random Entry!", bg=BBACKG, fg=FONTC, width=32, height=4, font="none 9 bold", command=search_func)
    random.place(relx=0.85, rely=0.41, anchor=S)

    recent_label = Label(UI, text="The 10 most recent searches!", bg=BACKG, fg=FONTC, font="none 12 bold")
    recent_label.place(relx=0.16, rely=0.23, anchor=S)

    # For the 10 most recent searches
    for i in range(0,10):
        if i <= 4:
            x = 0.08
            y = 0
        else:
            x = 0.23
            y = 0.25
        recent_searches.append(Button (UI, text=(f"Button: {i + 1}"), bg=BBACKG, fg=FONTC, width=16, font="none 9 bold", command=search_func))
        recent_searches[i].place(relx=x, rely=(i / 20) + 0.28 - y, anchor=S)
    
    with open(FILE, "r") as dict:
        lines = dict.readlines()
        for line in lines:
            dict_items.insert(END, line.strip("\n"))


#   test lababelfor potext=("a\na\na\na\na\na\na\na\nawidtwidth="nonfont="none 9 bold
#   test.place(relxi, textrely\na\na\anchorna\na\na\na"), width=16, font="none 9 bold")
#   test.placabellx=0.2text=("a\na\na\na\na\na\na\na\nae 9 widthfont=font="none 9 bold
#   test2.place(relxi, textrely\na\na\anchorna\na\na\na"), width=16, font="none 9 bold")
#   test2.plaabelelx=0.textrely=0.widthnchorheight"grebg="green", font="none 9 bold
#   test3.place(relxi, textrely), widthanchoreight=9, bg="green", font="none 9 bold")
#   test3.plaabelelx=0.textrely=0.widthanchoheight="grbg="green", font="none 9 bold
#   test4.place(relxi, textrely), widthanchoreight=9, bg="green", font="none 9 bold")
#   test4.place(relx=0.25, rely=0.647, anchor=s)
#   setting a list of all the widgets to delete all widgets
    widgets = [dict_label, scrollbar, dict_items, info_label, entry_box, error_label,
    search, add_word_button, random, recent_label]
# destroy function for main page
def destroy_main(widgets, recents_button):
        for i, j in zip(widgets, recents_button):
            i.destroy()
            j.destroy()

main_page()
UI.mainloop()