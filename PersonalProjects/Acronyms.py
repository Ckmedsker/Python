from tkinter import *


# Static Variables
BACKG = "#808080"
BBACKG = "#02babd"
FONTC = "black"
FILE = r"C:\Users\Camer\Documents\Cam's Vault\Cyber Academy\Cybersecurity Acronyms.md"
BACKUP = r"C:\Users\Camer\Desktop\Other\Backup\Cybersecurity Acronyms.md"
PHOTO = r"C:\Users\Camer\Pictures\color.png" 
if FILE == "" or BACKUP == "":
    print("Please specify the appropriate files!")
    exit()

# UI Initialization
UI = Tk()
UI.title("Acronyms")
UI.configure(bg=BACKG)
UI.geometry("1000x825")
UI.minsize(1000, 825)
UI.maxsize(1000, 825)
UI.iconphoto(False, PhotoImage(file=PHOTO))
info_label = Button(UI)


# functions
def search(a):
    global info_label
    bool = False
    info = ""
    info_label.destroy()
    entry = acronym_entry.get().lower()
    entry = (f"{entry} - ")
    c = 0
    if entry != (" - "):
        with open(FILE, "r") as ac:
            lines = ac.readlines()
            for line in lines:
                c += 1
                acr = line[0:len(entry)].lower()
                if acr == entry:
                    acronyms.see(c-1)
                    bool = True
            if bool == True:
                acronym_entry.delete(0, END)
                info = "The acronym was found!"
                error_color = "green"
            else:
                info = "The acronym is not found."
                error_color = "red"
    else:
        info = "Please enter an acronym!"
        error_color = "red"
    info_label = Label(UI, text=info, bg=BACKG,
                        fg=error_color, font="none 12 bold")
    info_label.place(relx=0.5, rely=0.815, anchor=S)

def add_acronym(a):
    global info_label
    found = False
    c = 0
    info_label.destroy()
    a_entry = acronym_entry.get().lower()
    w_entry = word_entry.get().lower()
    if w_entry != "":
        w_entry = list(w_entry)
        w_entry[0] = str(w_entry[0]).upper()
        for i, char in enumerate(w_entry): 
            if char == " " or char == "-":
                w_entry[i + 1] = str(w_entry[i + 1]).upper()
        w_entry = (''.join(w_entry))
    acdef = (f"{acronym_entry.get().upper()} - {w_entry}\n")
    if acdef == " - \n":
        info = "Please enter an acronym and definition!"
        error_color = "red"
    else:
        if w_entry == "":
            info = "Please enter a definition!"
            error_color = "red"
        else:
            if a_entry == "":
                info = "Please enter an acronym!"
                error_color = "red"
            elif a_entry != "":
                with open(FILE, "r") as ac:
                    lines = ac.readlines()
                    a_entry = f"{a_entry} - "
                    for line in lines:
                        c += 1
                        acr = (f"{line[0:len(a_entry)].lower()}")
                        if acr == a_entry:
                            acronyms.see(c-1)
                            found = True
                    c = 0
                    if found == True:
                        info = "This acronym is already on the list!"
                        error_color = "red"
                    elif found == False:
                        info = "Successfully added an acronym!"
                        error_color = "green"
                        acronyms.delete(0, END)
                        lines.append(acdef)
                        lines.sort()
                        with open(FILE, "w+") as ac:
                            with open(BACKUP, "w+") as back:
                                for line in lines:
                                    ac.write(line)
                                    back.write(line)
                                    acronyms.insert(END, line)
                        for i, line in enumerate(lines):
                            if acdef == line:
                                acronyms.see(i)

    acronym_entry.delete(0, END)
    word_entry.delete(0, END)
    info_label = Label(UI, text=info, bg=BACKG,
                        fg=error_color, font="none 12 bold")
    info_label.place(relx=0.5, rely=0.815, anchor=S)


# Main Page
main_label = Label(UI, text="Acronyms", bg=BACKG,
                   fg=FONTC, font="none 35 bold")
main_label.place(relx=0.5, rely=0.01, anchor=N)

scrollbar = Scrollbar(UI, orient="vertical")

acronyms = Listbox(UI, bg=BBACKG, fg=FONTC, width=95, height=23,
                   font="none 12 bold", highlightbackground=BACKG, yscrollcommand=scrollbar.set)
acronyms.place(relx=0.5, rely=0.08, anchor=N)

center_label = Label(UI, bg="#f83f4c", width=2, height=1)
center_label.place(relx=0.052, rely=0.358, anchor=W)

static_info_label = Label(UI, text="Type in an acronym to search it, or add a new acronym.",
                   bg=BACKG, fg=FONTC, font="none 12 bold")
static_info_label.place(relx=0.5, rely=0.68, anchor=S)

acronym_entry = Entry(UI, bg=BBACKG, fg=FONTC, width=10, font="none 20 bold")
acronym_entry.bind("<Return>", search)
acronym_entry.place(relx=0.5, rely=0.73, anchor=S)

word_entry = Entry(UI, bg=BBACKG, fg=FONTC, width=30, font="none 20 bold")
word_entry.bind("<Return>", add_acronym)
word_entry.place(relx=0.5, rely=0.78, anchor=S)

search_button = Button(UI, text="Search", bg=BBACKG, fg=FONTC,
                width=20, height=4, font="none 10 bold", command=lambda:search(""))
search_button.place(relx=0.4, rely=0.91, anchor=S)

add_word_button = Button(UI, text="Add Acronym", bg=BBACKG, fg=FONTC,
                         width=20, height=4, font="none 10 bold", command=lambda:add_acronym(""))
add_word_button.place(relx=0.6, rely=0.91, anchor=S)


with open(FILE, "r") as items:
    lines = items.readlines()
    for line in lines:
        acronyms.insert(END, line.strip("\n"))
UI.mainloop()
