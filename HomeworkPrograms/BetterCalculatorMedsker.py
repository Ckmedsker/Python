print("Welcome to Cam's Better Calculator!")
q = "y"
numb = []
answer = 0

#about the name below, I just wanted a name to represent input, without actually using the function name
def inputment():
    while True:
            try:
                numb.append(int(input("Please enter a number!\n")))
                break
            except ValueError:
                print("ERR---RROR... Please enter a whole number!")

while q == "y" or q == "":
    while True:
        if answer != 0:
            numb.clear()
            numb.append(answer)
        else:
            inputment()
        inputment()
        while True:
            print("What operation would you like performed?")
            print("Enter the symbol following for the corresponding operation!")
            choice = input("Addition|+\nSubtraction|-\nMultiplication|*\nDivision|/\n")
            if choice == "+":
                answer = sum(numb)
                print(f"The answer to your problem is:{answer}")
                break
            elif choice == "-":
                answer = numb[0] - numb[1]
                print(f"The answer to your problem is:{answer}")
                break
            elif choice == "*":
                answer = numb[0] * numb[1]
                print(f"The answer to your problem is:{answer}")
                break
            elif choice == "/":
                if numb[1] == 0:
                    print("A number divided by 0 is undefined!")
                    break
                else:
                    answer = numb[0] / numb[1]
                    print(f"The answer to your problem is: {answer}")
                    break
            else:
                continue

        q = input("Add another?: ")
        if q == "y" or q == "":
            continue
        else:
            break

