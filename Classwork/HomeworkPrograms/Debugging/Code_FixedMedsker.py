#below is a checker if the user input is a question or not.
def is_num(question):
    while True:
        try:
            x = int(input(question))
            break
        except ValueError:
            #below there is an error in the input, so it tells the user
            print("That is not a number")
            continue
    return x
#below is a class that creates all the variables for the user inputs
class cat():
    def __init__(self):
        self.name = input("\nWhat is your pet's name?\n")
        self.type = input(f"What type of pet is {self.name}?\n").lower()
        self.color = input(f"What color is {self.name}?\n").lower()
        self.age = is_num(f"How old is {self.name}?\n")
#below is the bulk of the code. It also contains a while loop to run a lot of the code multiple times until the user says not to
def main():
    pet = []
    response = "y"
    #below the program gets the user's name
    name = input("Hello! What is your name?\n")
    while response != "n":
        pet.append(cat())
        while True:
            #below the program asks if the user has another pet, and keeps runs part of the program again if the answer is yes
            response = input("\nDo you have another pet? Y|n: ").lower()
            if response == "y" or response == "":
                break
            elif response == "n":
                break
            else:
                #below the program asks if the user inputs something different into the textbox and returns back to them if they did
                print("\nYou did not make a correct response, please use a 'Y' for yes and a 'n' for no.")
                continue
    num_pets = len(pet)
    #below the program creates/opens a program to write all the data too
    with open('My_Pet_List.txt','w') as file:
        if num_pets == 1:
            #below the program writes to the file if the user only has one pet
            file.write(f"{name} has one pet, it's name is {pet[0].name}.\n\n")
        else:
            #below the program writes to the file if the user has more than one pet
            file.write(f"{name} has {num_pets} pets. Those pet's names are:")
            count = 0
            for i in pet:
                count += 1
                if count == 1:
                    #below the program writes the name of the pet to the file
                    file.write(f" {i.name}")
                elif count != 1:
                    # below the program writes the name of the pet to the file
                    file.write(f", {i.name}")
            #below the program writes to the file a period and 2 blank lines to be more readable
            file.write(".\n\n")
        for i in pet:
            #below the program writes the name, color, type and age of the pet to the file
            file.write(f"{i.name} is a {i.color} {i.type} and is {i.age} years old.\n")
main()

if __name__ != "__main__":
    main()
else: 
    exit
