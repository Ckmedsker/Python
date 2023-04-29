from tkinter import *
import math

BACKG = "green"
BBACKG = "gray"
FONTC = "black"

UI = Tk()
UI.title("Portal Coords")
UI.configure(bg=BACKG)
UI.geometry("1200x825")
UI.minsize(1200, 825)
UI.maxsize(1200, 825)

boxes = []
values = []
total = 0

def calculate_coords():
    global total, values
    count = 0
    for box in boxes:
        box_value = box.get()
        box.delete(0, END)
        if box_value != "":
            if count == 0:
                ones_values = int(box_value)
                values.append(ones_values)
            elif count == 1:
                fives_values = int(box_value) * 5
                values.append(fives_values)
            elif count == 2:
                tens_values = int(box_value) * 10
                values.append(tens_values)
            elif count == 3:
                twenties_values = int(box_value) * 20
                values.append(twenties_values)
            elif count == 4:
                pennies_values = int(box_value) * .01
                values.append(pennies_values)
            elif count == 5:
                nickels_values = int(box_value) * .05
                values.append(nickels_values)
            elif count == 6:
                dimes_values = int(box_value) * .1
                values.append(dimes_values)
            elif count == 7:
                quarters_values = int(box_value) * .25
                values.append(quarters_values)
        count += 1
    for value in values:
        print(value)
    print(f"Values:{values}")
    print(f"Sum of Values:{sum(values)}")
    if total != 0:
        total = total + sum(values)
        print(total)
    else:
        total = sum(values)
        print(total)
    info_display_label.config(text = f"${total:,}")
    values = []
    
def clear():
    global total
    total = 0
    info_display_label.config(text = "Press Calculate!")
    for box in boxes:
        box.delete(0, END)


# Graphics
main_label = Label(UI, text="Money Calculator", bg=BACKG,
                   fg=FONTC, font="none 35 bold")
main_label.place(relx=0.5, rely=0.25, anchor=N)

ones_label = Label(UI, text="Ones", bg=BACKG,
                   fg=FONTC, font="none 20 bold")
ones_label.place(relx=0.35, rely=0.35, anchor=N)

fives_label = Label(UI, text="Fives", bg=BACKG,
                   fg=FONTC, font="none 20 bold")
fives_label.place(relx=0.45, rely=0.35, anchor=N)

tens_label = Label(UI, text="Tens", bg=BACKG,
                   fg=FONTC, font="none 20 bold")
tens_label.place(relx=0.55, rely=0.35, anchor=N)

twenties_label = Label(UI, text="Twenties", bg=BACKG,
                   fg=FONTC, font="none 20 bold")
twenties_label.place(relx=0.65, rely=0.35, anchor=N)

pennies_label = Label(UI, text="Pennies", bg=BACKG,
                   fg=FONTC, font="none 20 bold")
pennies_label.place(relx=0.35, rely=0.45, anchor=N)

nickels_label = Label(UI, text="Nickels", bg=BACKG,
                   fg=FONTC, font="none 20 bold")
nickels_label.place(relx=0.45, rely=0.45, anchor=N)

dimes_label = Label(UI, text="Dimes", bg=BACKG,
                   fg=FONTC, font="none 20 bold")
dimes_label.place(relx=0.55, rely=0.45, anchor=N)

quarters_label = Label(UI, text="Quarters", bg=BACKG,
                   fg=FONTC, font="none 20 bold")
quarters_label.place(relx=0.65, rely=0.45, anchor=N)

ones_box = Entry(UI, bg=BBACKG, fg=FONTC, width=5, font="none 20 bold")
ones_box.place(relx=0.35, rely=0.45, anchor=S)
boxes.append(ones_box)

fives_box = Entry(UI, bg=BBACKG, fg=FONTC, width=5, font="none 20 bold")
fives_box.place(relx=0.45, rely=0.45, anchor=S)
boxes.append(fives_box)

tens_box = Entry(UI, bg=BBACKG, fg=FONTC, width=5, font="none 20 bold")
tens_box.place(relx=0.55, rely=0.45, anchor=S)
boxes.append(tens_box)

twenties_box = Entry(UI, bg=BBACKG, fg=FONTC, width=5, font="none 20 bold")
twenties_box.place(relx=0.65, rely=0.45, anchor=S)
boxes.append(twenties_box)

pennies_box = Entry(UI, bg=BBACKG, fg=FONTC, width=5, font="none 20 bold")
pennies_box.place(relx=0.35, rely=0.55, anchor=S)
boxes.append(pennies_box)

nickels_box = Entry(UI, bg=BBACKG, fg=FONTC, width=5, font="none 20 bold")
nickels_box.place(relx=0.45, rely=0.55, anchor=S)
boxes.append(nickels_box)

dimes_box = Entry(UI, bg=BBACKG, fg=FONTC, width=5, font="none 20 bold")
dimes_box.place(relx=0.55, rely=0.55, anchor=S)
boxes.append(dimes_box)

quarters_box = Entry(UI, bg=BBACKG, fg=FONTC, width=5, font="none 20 bold")
quarters_box.place(relx=0.65, rely=0.55, anchor=S)
boxes.append(quarters_box)

calculate_button = Button(UI, text="Calculate", bg=BBACKG, fg=FONTC,
                width=10, height=1, font="none 20 bold", command=lambda:calculate_coords())
calculate_button.place(relx=0.4, rely=0.65, anchor=S)

clear_button = Button(UI, text="Clear", bg=BBACKG, fg=FONTC,
                width=10, height=1, font="none 20 bold", command=lambda:clear())
clear_button.place(relx=0.6, rely=0.65, anchor=S)

info_display_label = Label(UI, text="Press Calculate!",
                   bg=BACKG, fg=FONTC, font="none 30 bold")
info_display_label.place(relx=0.5, rely=0.8, anchor=S)

UI.mainloop()