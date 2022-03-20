pets = []


class Pet:
    def __init__(self):
        self.type = input(f"What type of animal do you want to have?: ")
        self.name = input(f"What is the pet's name?: ")
        self.breed = input(f"What is {self.name}'s breed?: ")
        self.color = input(f"What is {self.name}'s color?: ")


while True:

    choice = input("Would you like to add a pet? Y|n\n").lower()
    if choice == "y" or choice == "":
        pets.append(Pet())
        continue
    elif choice == "n":
        for i in range(len(pets)):
            print(f"{pets[i].name} is a {pets[i].type}, and is a {pets[i].breed} breed and is the color {pets[i].color}!")
        break
    else:
        print("Please input a valid choice!!! ")