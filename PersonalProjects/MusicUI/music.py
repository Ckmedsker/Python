from tkinter import *
from os.path import exists

# Static Variables
FILE = "song.txt"
FILE1 = "temp.txt"
IMAGE = r"C:\Users\Camer\Pictures\music_note.png"
BACKG = "black"
BBACKG = "brown"
FOREG = "red"
FONTC = "white"


# UI Initialization
UI = Tk()
UI.title("Music Player/Creater")
UI.configure(bg=BACKG)
UI.geometry("1000x825")
UI.minsize(1000, 825)
UI.maxsize(1000, 825)
UI.iconphoto(False, PhotoImage(file=IMAGE))

# Initialization
if FILE == "" or FILE1 == "":
    print("Please specify the appropriate files!")
    exit()
def file_checker():
    if not exists(FILE):
        open(FILE, "w")
    if not exists(FILE1):
        open(FILE1, "w")
file_checker()

# Setting up the main page
def main():
    main_label = Label(UI, text="Music Player/Creater")

# Setting up the play page


# Setting up the create page


UI.mainloop()

