classes = []
dashes = []
for i in range(30):
    dashes.append("-")

class AddClass:
    def __init__(self):
        global dashesP
        self.name = input("What is the class name?\n")
        self.sName = []
        self.grade = []
        self.gradeN = []
        self.dashesP = []
        while True:
            if len(self.sName) == 0 or len(self.grade) == 0:
                choice1 = ""
                pass
            else:
                choice1 = input("Would you like to add another student's grades? Y|n: ").lower()
            if choice1 == "y" or choice1 == "":
                while True:
                    s = input("What is the student's name?: ").upper()
                    if len(s) > 25:
                        print("Please enter a smaller name!")
                        continue
                    else:
                        break
                lList = list(s)
                for i in range(len(lList)):
                    dashes.pop(i)
                self.dashesP.append("".join(dashes))
                for _ in lList:
                    dashes.append("-")
                self.sName.append(s)
                while True:
                    g = input("What is the student's grade? \nEnter A|B|C|D|F\n").upper()
                    if g == "A":
                        self.gradeN.append(4)
                        self.grade.append(g)
                        break
                    elif g == "B":
                        self.gradeN.append(3)
                        self.grade.append(g)
                        break
                    elif g == "C":
                        self.gradeN.append(2)
                        self.grade.append(g)
                        break
                    elif g == "D":
                        self.gradeN.append(1)
                        self.grade.append(g)
                        break
                    elif g == "F":
                        self.gradeN.append(0)
                        self.grade.append(g)
                        break
                    else:
                        print("Invalid Input!")
                        continue
            elif choice1 == "n" and len(self.sName) == 0 or len(self.grade) == 0:
                print("There is no students or grades entered!")
                continue
            elif choice1 == "n":
                break


def printG():
    count = 0
    while True:
        print(f"            {classes[count].name}\n")
        for i in range(len(classes[count].sName)):
            print(f"{classes[count].sName[i]}{classes[count].dashesP[i]}{classes[count].grade[i]}")
        if count == len(classes) - 1:
            break
        count += 1
    average = sum(classes[count].gradeN) / len(classes[count].gradeN)
    print(f"The class average on a 4.0 scale is: {average}\n\n")


def main():
    while True:
        print("Main Menu:")
        while True:
            try:
                choice = int(input("Check grades = 1.\nAdd a class = 2\nExit = 3.\n"))
                break
            except ValueError:
                print("Invalid Input! ")
                continue
        while True:
            if choice == 1:
                if len(classes) != 0:
                    printG()
                    print()
                    break
                else:
                    print("There is no grades to check!")
                    continue
                break
            elif choice == 2:
                classes.append(AddClass())
                printG()
                break
            elif choice == 3:
                exit()
            else:
                print("Invalid Input!")


print("Welcome to Cam High's Grading Book!\n")
main()