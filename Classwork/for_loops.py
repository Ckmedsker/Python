
my_list = []
while True:
    question = input("Add another?: \n Y|n: ").lower()
    if question in yes_list:
        my_list.append(input("Give me a friend's name: "))
        continue
    elif question == "n":
        break
    else:
        print(print("You did not select a y or n"))

for i in my_list:
    print(i + " is my friend! =)")