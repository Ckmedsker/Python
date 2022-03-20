name = []
age = []
q = "y"
while q == "y" or q == "":
    name.append(input("What is your friend's name?\n"))
    age.append(input("What is you friend's age?\n"))
    while True:
        q = input("Add another?: ")
        if q == "y" or q == "" or q == "n":
            continue
        else:
            break
print(name)
print(age)

for i, j in zip(name, age):
    print(f"You have a friend named {i} and they are {j} years old.")