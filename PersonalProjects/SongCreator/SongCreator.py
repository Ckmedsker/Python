from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
import os
import time


# Static Variables
REL_PATH = os.path.dirname(__file__) # Used to get the relative file path to be used throughout the program
ICON_PATH = fr"{REL_PATH}\Assets\Images\music_note.png" # File path for the Icon image that is also used as two images on the main page
MUSIC_SCALE_PATH = fr"{REL_PATH}\Assets\Images\music_scale.jpg"# File path for the Music Scale image used on the song creator page
NOTES_PATH = fr"{REL_PATH}\Assets\Notes" # Path to access the Notes
NOTES = ["A4.mp3", "Ab6.mp3", "Db3.mp3", "Db6.mp3", "E2.mp3", "F4.mp3", "Gb3.mp3"]
# A set of most symbols that will be used to check for user input.
symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '"', '*', '|',
',', '&', '<', '`', '}', '.', '=', ']', '!', '>', ';', '?', '#','$', ')', '/', ' ', '©']
BBACKG = "#007b72" # A good looking color to be used throughout as the main background
BACKG = "#87ceeb" # A good looking color to be used throughout as the background to many widgets
FONTC = "black" # Color to be used as the font color throughout


# UI Initialization
UI = Tk()
UI.title("Music Player/Creater")
UI.configure(bg=BACKG)
UI.geometry("1000x825")
UI.minsize(1000, 800) # Setting the minumium window size
UI.maxsize(1000, 800) # Setting the maximum window size
UI.iconphoto(False, PhotoImage(file=ICON_PATH))


# Image and Music Initialization
mixer.init()
musical_scale_image = Image.open(MUSIC_SCALE_PATH).resize((587, 146)) # Opening and resizing the musical scale image
musical_scale_image = ImageTk.PhotoImage(musical_scale_image) # Used to set the image as an image for tkinter
musical_note_image = Image.open(ICON_PATH) # Opening and resizing the musical note image
musical_note_image = ImageTk.PhotoImage(musical_note_image) # Used to set the image as an image for tkinter


# Variable Initialization
notes_and_timing = [] # List used to make song recording
notes = [] # List used to separate notes from notes_and_timing list
timings = [] # List used to separate timings from notes_and_timing list
timing_start2 = 0 # Used to create timings in between sets of button presses
main_page_status_label = Button(UI) # Button used throughout the main page to provide information to the user
song_creator_page_status_label = Button(UI) # Button used throughout the song creator page to provide information to the user
timing = False # Boolean value used to determine if the note buttons have been pressed to create timings
recording = False # Boolean value used to signify if the song creator is recording

# Clearing the terminal for looks
os.system('cls' if os.name == 'nt' else 'clear')


# Main page functionality
def create_main():

    # Destroys the main page and creates the song creator page
    def destroy_main_page(widgets):
        for widget in widgets:
            widget.destroy()
        # Calls the other page to be created
        create_song_creator()
        song_creator_page_status_label.destroy()

    # Plays the selected song
    def play_song():
        global song_creator_page_status_label
        songs = os.listdir(fr"{REL_PATH}\Songs") # Used to get a list of all files in the songs directory
        notes.clear()
        timings.clear()
        if songs_listbox.curselection() != ():
            song = songs[songs_listbox.curselection()[0]] # The selected song in the listbox
            with open(fr"{REL_PATH}\Songs\{song}", "r") as song:
                lines = song.readlines() # Gets the lines within the given text file as a list
                lines.pop(0) # Deletes the watermark so it can play the song
                for index, line in enumerate(lines):
                    line = line.strip("\n") # Removes new line characters to then be sort
                    if index % 2 != 0:
                        timings.append(float(line)) # Adds the timings into one list
                    elif index % 2 == 0:
                        notes.append(line) # Adds the notes into one list
                mixer.music.load(fr"{NOTES_PATH}\{NOTES[NOTES.index(notes[0])]}")
                mixer.music.play()
                notes.pop(0)

                for note, timing in zip(notes, timings):
                    time.sleep(timing)
                    mixer.music.load(fr"{NOTES_PATH}\{NOTES[NOTES.index(note)]}")
                    mixer.music.play()
        else:
            # Provides feedback to the user if there is no selected item
            song_creator_page_status_label.destroy()
            song_creator_page_status_label = Label(UI, text="Please select a song from the listbox to play! Click on an item to select it!",
                            bg=BACKG, fg="red", font="none 10 bold")
            song_creator_page_status_label.place(relx=0.5, rely=0.95, anchor=S)

    # Used to add all of the songs into the listbox
    def listbox_update():
        songs_listbox.delete(0, END)
        songs = os.listdir(fr"{REL_PATH}\Songs") # Used to get a list of all files in the songs directory
        for song in songs:
            songs_listbox.insert(END, os.path.splitext(song)[0]) # Adding the songs into the listbox


    # Used to delete the selected song
    def delete_selected_song():
        global song_creator_page_status_label
        songs = os.listdir(fr"{REL_PATH}\Songs") # Used to get a list of all files in the songs directory
        if songs_listbox.curselection() != ():
            os.remove(fr"{REL_PATH}\Songs\{songs[songs_listbox.curselection()[0]]}") # Deletes the selected song
            listbox_update() # Updates the listbox to remove the removed song
        else:
            # Provides feedback to the user if there is no selected item
            song_creator_page_status_label.destroy()
            song_creator_page_status_label = Label(UI, text="Please select a song from the listbox to delete! Click on an item to select it!",
                            bg=BACKG, fg="red", font="none 10 bold")
            song_creator_page_status_label.place(relx=0.5, rely=0.95, anchor=S)



    # Creating the widgets for the main page
    exit_button = Button(UI, text="Exit!", bg=BBACKG,
                           fg=FONTC, width=20, height=5, font="none 8 bold", command=UI.quit)
    exit_button.place(relx=0.085, rely=0.11, anchor=S)

    main_info_label = Label(UI, text="Cam's Song Creator!",
                       bg=BACKG, fg=FONTC, font="none 36 bold")
    main_info_label.place(relx=0.5, rely=0.1, anchor=S)

    description_label = Label(UI, text="Click on a song below and then click the Play Selected Song button!\nClick on the Create Song button to make your own songs!",
                       bg=BACKG, fg=FONTC, font="none 14 bold")
    description_label.place(relx=0.5, rely=0.16, anchor=S)

    music_note_image_label1 = Label(UI, image=musical_note_image ,text="Music Note Image 1",
                       bg=BACKG, fg=FONTC, font="none 14 bold", width=200, height=200)
    music_note_image_label1.place(relx=0.135, rely=0.6, anchor=S)

    scrollbar = Scrollbar(UI, orient="vertical")

    songs_listbox = Listbox(UI, bg=BBACKG, fg=FONTC, width=35, height=15,
                         font="none 20 bold", highlightbackground=BACKG, yscrollcommand=scrollbar.set)
    songs_listbox.place(relx=0.5, rely=0.16, anchor=N)

    music_note_image_label2 = Label(UI, image=musical_note_image, text="Music Note Image 2",
                       bg=BACKG, fg=FONTC, font="none 14 bold", width=200, height=200)
    music_note_image_label2.place(relx=0.865, rely=0.6, anchor=S)

    delete_button = Button(UI, text="Delete Selected Song!", bg=BBACKG,
                           fg=FONTC, width=30, height=5, font="none 8 bold", command=delete_selected_song)
    delete_button.place(relx=0.25, rely=0.9, anchor=S)

    play_button = Button(UI, text="Play Selected Song!", bg=BBACKG,
                           fg=FONTC, width=30, height=5, font="none 8 bold", command=play_song)
    play_button.place(relx=0.5, rely=0.9, anchor=S)

    create_button = Button(UI, text="Create Song!", bg=BBACKG,
                           fg=FONTC, width=30, height=5, font="none 8 bold", command=lambda:destroy_main_page(main_page_widgets))
    create_button.place(relx=0.75, rely=0.9, anchor=S)



    listbox_update() # Updates the listbox on initization and when the main page is called
    # List of all the widgets within the main page. Used to destroy them
    main_page_widgets = [exit_button, main_info_label, description_label, scrollbar, songs_listbox,
    delete_button, play_button, create_button, song_creator_page_status_label, music_note_image_label1, music_note_image_label2]




# Setting up the create page
def create_song_creator():

    # Destroys the creator_page, then rebuilds the main page with updated information
    def destroy_creator_page(widgets):
        main_page_status_label.destroy()
        entry = name_box.get() # Gets the entry from the textbox
        if entry != "": # If there is nothing within the textbox, nothing gets saved
            notes_and_timing.pop(0)
            notes_and_timing.insert(0, f"Created by Cam's Song Creator! Song Name: {entry}") # Watermark for fun, and to identify files
            with open(fr"{REL_PATH}\Songs\{entry}.txt", "w+") as song:
                for line in notes_and_timing:
                    song.write(f"{line}\n")

        for widget in widgets:
            widget.destroy()
        # Taking away the bindings of the buttons so they cannot be played on
        # the main page, and they will not be played when trying to type in the
        # name of the song on the song creator page
        note1_button.unbind_all("a")
        note2_button.unbind_all("s")
        note3_button.unbind_all("d")
        note4_button.unbind_all("f")
        note5_button.unbind_all("j")
        note6_button.unbind_all("k")
        note7_button.unbind_all("l")
        create_main()


    # Used to play, and then log the notes to be replayed
    def notes(note_numb):
        global timing, timing_start1, timing_start2
        # Used to play the notes that is indicated with note_numb
        mixer.music.load(fr"{NOTES_PATH}\{NOTES[note_numb - 1]}")
        mixer.music.play()
        if recording == True:
            # A flip-flop to determine when to time things
            if timing == False:
                notes_and_timing.append(time.time() - timing_start2)
                timing_start1 = time.time() # Gets the current time to later be subtracted from the current time then
                notes_and_timing.append(NOTES[note_numb - 1])
                timing = True # Alternating the timing Boolean

            elif timing == True:
                notes_and_timing.append(time.time() - timing_start1)
                notes_and_timing.append(NOTES[note_numb - 1])
                timing_start2 = time.time() # Gets the current time to later be subtracted from the current time then
                timing = False # Alternating the timing Boolean

        
    # When the start/stop song button is clicked, the song recording begins/pauses
    def record_song():
        global recording, main_page_status_label
        entry = name_box.get() # Gets the text within the name box
        if entry == "":
            status = "Please enter a name for the song!" # Sets the text to be displayed soon
            status_color = "red" # A color to visually represent to the user what is good and bad feedback
            main_page_status_label.destroy()
            main_page_status_label = Label(UI, text=status, fg=status_color, bg=BACKG, font="none 14 bold")
            main_page_status_label.place(relx=0.5, rely=0.94, anchor=S)
        else:
            for sym in symbols:
                if sym in entry:
                    status = "You can't use any symbols other than underscores!" # Sets the text to be displayed soon
                    status_color = "red" # A color to visually represent to the user what is good and bad feedback
                    main_page_status_label.destroy()
                    main_page_status_label = Label(UI, text=status, fg=status_color, bg=BACKG, font="none 14 bold")
                    main_page_status_label.place(relx=0.5, rely=0.94, anchor=S)
                    break
            else:
                if recording == False:
                    recording = True # Toggles the recording
                    name_box.config(state='disabled')
                    note1_button.bind_all("a", lambda event : notes(1))
                    note2_button.bind_all("s", lambda event : notes(2))
                    note3_button.bind_all("d", lambda event : notes(3))
                    note4_button.bind_all("f", lambda event : notes(4))
                    note5_button.bind_all("j", lambda event : notes(5))
                    note6_button.bind_all("k", lambda event : notes(6))
                    note7_button.bind_all("l", lambda event : notes(7))
                    status = "Recording!" # Sets the text to be displayed soon
                    status_color = "green" # A color to visually represent to the user what is good and bad feedback
                    main_page_status_label.destroy()
                    main_page_status_label = Label(UI, text=status, fg=status_color, bg=BACKG, font="none 14 bold")
                    main_page_status_label.place(relx=0.5, rely=0.94, anchor=S)
                elif recording == True:
                    recording = False # Toggles the recording
                    main_page_status_label.destroy()


    # Button used to delete the song that is currently being recorded
    def delete_song():
        global recording, main_page_status_label
        if notes_and_timing != []:
            notes_and_timing.clear()
            name_box.config(state='normal')
            main_page_status_label.destroy()
            main_page_status_label = Label(UI, text="Successful deleted current recording.", fg="green", bg=BACKG, font="none 14 bold")
            main_page_status_label.place(relx=0.5, rely=0.94, anchor=S)
            recording = False
        else:
            main_page_status_label.destroy()
            main_page_status_label = Label(UI, text="There is no song being recorded!", fg="red", bg=BACKG, font="none 14 bold")
            main_page_status_label.place(relx=0.5, rely=0.94, anchor=S)

        


    main_info_label = Label(UI, text="Cam's Song Creator!",
                       bg=BACKG, fg=FONTC, font="none 36 bold")
    main_info_label.place(relx=0.5, rely=0.1, anchor=S)

    description_info_label = Label(UI, text="Press the start/stop button to begin recording!\n Press it again to stop recording!",
                       bg=BACKG, fg=FONTC, font="none 14 bold")
    description_info_label.place(relx=0.5, rely=0.17, anchor=S)
    
    exit_button = Button(UI, text="Exit!", bg=BBACKG,
                           fg=FONTC, width=20, height=5, font="none 8 bold", command=UI.quit)
    exit_button.place(relx=0.085, rely=0.11, anchor=S)
    
    start_stop_button = Button(UI, text="Start/Stop Recording!", bg=BBACKG,
                           fg=FONTC, width=20, height=5, font="none 8 bold", command=record_song)
    start_stop_button.place(relx=0.085, rely=0.44, anchor=S)

    delete_button = Button(UI, text="Delete Current Recording!", bg=BBACKG,
                           fg=FONTC, width=20, height=5, font="none 8 bold", command=delete_song)
    delete_button.place(relx=0.085, rely=0.56, anchor=S)

    musical_scale_image_label = Label(image=musical_scale_image, text = "Musical Scale with 7 notes!",
     width=587, height=146)
    musical_scale_image_label.place(relx=0.5, rely=0.55, anchor=S)

    note1_label = Label(UI, text=os.path.splitext(NOTES[0])[0],
                       bg=BACKG, fg=FONTC, font="none 14 bold")
    note1_label.place(relx=0.23, rely=0.65, anchor=S)

    note2_label = Label(UI, text=os.path.splitext(NOTES[1])[0],
                       bg=BACKG, fg=FONTC, font="none 14 bold")
    note2_label.place(relx=0.32, rely=0.65, anchor=S)

    note3_label = Label(UI, text=os.path.splitext(NOTES[2])[0],
                       bg=BACKG, fg=FONTC, font="none 14 bold")
    note3_label.place(relx=0.41, rely=0.65, anchor=S)

    note4_label = Label(UI, text=os.path.splitext(NOTES[3])[0],
                       bg=BACKG, fg=FONTC, font="none 14 bold")
    note4_label.place(relx=0.5, rely=0.65, anchor=S)

    note5_label = Label(UI, text=os.path.splitext(NOTES[4])[0],
                       bg=BACKG, fg=FONTC, font="none 14 bold")
    note5_label.place(relx=0.59, rely=0.65, anchor=S)

    note6_label = Label(UI, text=os.path.splitext(NOTES[5])[0],
                       bg=BACKG, fg=FONTC, font="none 14 bold")
    note6_label.place(relx=0.68, rely=0.65, anchor=S)

    note7_label = Label(UI, text=os.path.splitext(NOTES[6])[0],
                       bg=BACKG, fg=FONTC, font="none 14 bold")
    note7_label.place(relx=0.77, rely=0.65, anchor=S)

    note1_button = Button(UI, text="A", bg=BBACKG,
                           fg=FONTC, width=9, height=3, font="none 11 bold", command=lambda:notes(1))
    note1_button.place(relx=0.23, rely=0.75, anchor=S)

    note2_button = Button(UI, text="S", bg=BBACKG,
                           fg=FONTC, width=9, height=3, font="none 11 bold", command=lambda:notes(2))
    note2_button.place(relx=0.32, rely=0.75, anchor=S)

    note3_button = Button(UI, text="D", bg=BBACKG,
                           fg=FONTC, width=9, height=3, font="none 11 bold", command=lambda:notes(3))
    note3_button.place(relx=0.41, rely=0.75, anchor=S)

    note4_button = Button(UI, text="F", bg=BBACKG,
                           fg=FONTC, width=9, height=3, font="none 11 bold", command=lambda:notes(4))
    note4_button.place(relx=0.5, rely=0.75, anchor=S)

    note5_button = Button(UI, text="J", bg=BBACKG,
                           fg=FONTC, width=9, height=3, font="none 11 bold", command=lambda:notes(5))
    note5_button.place(relx=0.59, rely=0.75, anchor=S)

    note6_button = Button(UI, text="K", bg=BBACKG,
                           fg=FONTC, width=9, height=3, font="none 11 bold", command=lambda:notes(6))
    note6_button.place(relx=0.68, rely=0.75, anchor=S)

    note7_button = Button(UI, text="L", bg=BBACKG,
                           fg=FONTC, width=9, height=3, font="none 11 bold", command=lambda:notes(7))
    note7_button.place(relx=0.77, rely=0.75, anchor=S)


    name_box_label = Label(UI, text="Enter in the name of your song,\nthen click on the Start/Stop recording button!",
                       bg=BACKG, fg=FONTC, font="none 14 bold")
    name_box_label.place(relx=0.5, rely=0.83, anchor=S)

    save_button = Button(UI, text="Back Home and Save Song!", bg=BBACKG,
                           fg=FONTC, width=20, height=5, font="none 8 bold", command=lambda:destroy_creator_page(create_page_widgets))
    save_button.place(relx=0.085, rely=0.9, anchor=S)

    name_box = Entry(UI, bg=BBACKG, fg=FONTC, width=35, font="none 20 bold")
    name_box.place(relx=0.5, rely=0.9, anchor=S)

    

    # List used to iterate through the various widgets to get destroyed.
    create_page_widgets = [main_info_label, exit_button, start_stop_button, 
    delete_button, note1_label, note2_label, note3_label, note4_label,
    note5_label, note6_label, note7_label, note1_button,
    note2_button, note3_button, note4_button, note5_button, note6_button,
    note7_button, main_page_status_label, save_button, name_box, description_info_label,
    musical_scale_image_label, name_box_label]


# Creates the main page for the first run-through
create_main()

# Tkinter Initization
UI.mainloop()