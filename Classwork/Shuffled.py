from random import shuffle as sh
import os

os.system("cls" if os.name == "nt" else "clear")

my_list = ["Apple", "Banana", "Cherry", "Date", "Fig", "Gundam"]
print(my_list)
element = my_list.index("Gundam")
print(element)
sh(my_list)
print(my_list)
element = my_list.index("Gundam")
print(element)