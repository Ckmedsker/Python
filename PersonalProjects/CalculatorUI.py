from tkinter import *


backG = "black"
foreG = "white"
equationV = []
temp = []

def out(var):
    output.configure(state="normal")
    output.delete(0.0, END)
    output.insert(END, var)
    output.configure(state="disabled")

def click(numb):
    temp.append(numb)
    out(temp)

def neg():
    if temp[0] == "-":
        out(temp)
    else:
        temp.insert(0,"-")
        out(temp)

def dec():
    if temp[0] == ".":
        out(temp)
    else:
        temp.append(".")
        out(temp)

def calc(math):
    if math == "+" or math == "-" or math =="*" or math =="/":
        equationV.append(''.join(map(str, temp)))
        temp.clear()
        equationV.append(math)
    elif math == "=":
        if len(equationV) == 1:
            out(temp)
        if len(temp) != 0:
            equationV.append(''.join(map(str, temp)))
            temp.clear()
        for i,equ in enumerate(equationV):
            if equ == '':
                equationV.pop(i)
        out(equationV)
        equation = (' '.join(equationV))
        out(''.join(map(str, (f"{equation} = {eval(equation)}"))))

def clear():
    equationV.clear()
    temp.clear()
    out(temp)

calculator = Tk()
calculator.title("Calculator")
calculator.configure(bg=backG)
calculator.geometry("840x597")

output = Text(calculator, width=50, height=4, wrap=WORD, bg=backG, fg=foreG, font="none 30")
output.grid(row=0, column=0, columnspan=1000)
output.configure(state="disabled")

Button (calculator, text="7", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:click(7)) .grid(row=1,column=0)
Button (calculator, text="8", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:click(8)) .grid(row=1,column=1)
Button (calculator, text="9", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:click(9)) .grid(row=1,column=2)
Button (calculator, text="+", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:calc("+")) .grid(row=1,column=3)
Button (calculator, text="-", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:calc("-")) .grid(row=1,column=4)
Button (calculator, text="4", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:click(4)) .grid(row=2,column=0)
Button (calculator, text="5", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:click(5)) .grid(row=2,column=1)
Button (calculator, text="6", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:click(6)) .grid(row=2,column=2)
Button (calculator, text="x", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:calc("*")) .grid(row=2,column=3)
Button (calculator, text="/", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:calc("/")) .grid(row=2,column=4)
Button (calculator, text="1", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:click(1)) .grid(row=3,column=0)
Button (calculator, text="2", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:click(2)) .grid(row=3,column=1)
Button (calculator, text="3", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:click(3)) .grid(row=3,column=2)
Button (calculator, text="-x",width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=neg) .grid(row=2,column=6)
Button (calculator, text="=", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:calc("=")) .grid(row=3,column=6)
Button (calculator, text="0", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=lambda:click(0)) .grid(row=3,column=3)
Button (calculator, text="C", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=clear) .grid(row=3,column=4)
Button (calculator, text=".", width=10, height=5, font="none 16 bold", bg=backG, fg=foreG, command=dec) .grid(row=1,column=6)


calculator.mainloop()