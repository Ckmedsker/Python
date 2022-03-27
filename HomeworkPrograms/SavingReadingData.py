import os.path

if os.path.exists("goba.txt"):
    with open("goba.txt","r") as rFile:
        for line in rFile:
            if line == ("good"):
                print("I'm glad your day was good!")
            elif line == ("bad"):
                print("I'm sorry your day was bad...")
with open("goba.txt","w+") as file:
    while True:
        input = input("How is your day? Is it good or bad?\n").lower()
        if input == "good":
            file.write("good")
            break
        elif input == "bad":
            file.write("bad")
            break
        else:
            print("Please enter good or bad!")
            continue