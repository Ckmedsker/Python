from tkinter import *

# Static Variables
BACKG = "black"
FOREG = "white"

# Varible Initialization
recent_searches = []
test2 = 0

# UI Initialization
UI = Tk()
UI.title("Dictionary")
UI.configure(bg=BACKG)
UI.geometry("1000x850")
UI.minsize(1000, 850)

# Making the visuals for the Main Page
def main_page():
    def search_func():
        dict_items.insert(1, "test")

    global dict_label, scrollbar, dict_items, info_label, entry_box, info_label, entry_box, error_label
    global search, add_word, random, recent_searches
    dict_label = Label (UI,text="Dictionary", bg=BACKG, fg=FOREG, font="none 24 bold")
    dict_label.place(relx=0.5, rely=0.01, anchor=N)

    scrollbar = Scrollbar(UI, orient="vertical")
    
    dict_items = Listbox(UI, bg=BACKG, fg=FOREG, width=60, height=30, yscrollcommand=scrollbar.set)
    dict_items.place(relx=0.5, rely=0.08, anchor=N)

    info_label = Label (UI,text="Type in the entry box to search or add definitions!", bg=BACKG, fg=FOREG, font="none 12 bold")
    info_label.place(relx=0.5, rely=0.68, anchor=S)

    entry_box = Entry(UI, width=20, font="none 20 bold")
    entry_box.place(relx=0.5, rely=0.76, anchor=S)

    error_label = Label (UI,text="", bg=BACKG, fg=FOREG, font="none 12 bold")
    error_label.place(relx=0.5, rely=0.81, anchor=S)

    search = Button (UI, text="Search", width=24, height=4, font="none 9 bold", command=search_func)
    search.place(relx=0.4, rely=0.91, anchor=S)

    add_word = Button (UI, text="Add Word", width=24, height=4, font="none 9 bold", command=search_func)
    add_word.place(relx=0.6, rely=0.91, anchor=S)

    random = Button (UI, text="Go To Random Entry!", width=32, height=4, font="none 9 bold", command=search_func)
    random.place(relx=0.85, rely=0.41, anchor=S)

    for i in range(0,10):
        if i <= 4:
            x = 0.08
            y = 0
        else:
            x = 0.23
            y = 0.25
        recent_searches.append(Button (UI, text=(f"Button: {i + 1}"), width=16, font="none 9 bold", command=search_func))
        recent_searches[i].place(relx=x, rely=(i / 20) + 0.28 - y, anchor=S)

    #global dict_label, scrollbar, dict_items, info_label, entry_box, info_label, entry_box, error_label
    #global search, add_word, random, recent_searches

# Destroy function for main page
def destroy_main():
    pass

# Main Loop
main_page()
UI.mainloop()