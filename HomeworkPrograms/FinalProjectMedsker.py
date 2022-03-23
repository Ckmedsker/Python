values = {"hundreds":100, "fifties":50, "twenties":20, "tens":10, "fives":5, "ones":1, "quarters":0.25, "dimes":0.10, "nickels":0.05, "pennies":0.01}
storetotal = {}
storesum = []
count = 0
dashes = []
dashesP = []
for i in range(30):
    dashes.append("-")

#below is a function for getting user input for each money value. It corresponds to the dictonary above and the name of the store
def bills(storename):
    for i, k in zip(values.keys(), values.values()):
        while True:
            try:
                x = int(input(f"How many {i} are in the system at {storename}?: "))
                storesum.append(x * k)
                break
            except ValueError:
                print("Please enter a number!")
                continue
        storetotal.update({storename:round(sum(storesum),2)})

#below is a function for printing/saving the totals
def totals(operation, line):
    global count
    operation(f"STORE TOTALS{line}")
    for l, m in zip(storetotal.keys(), storetotal.values()):
        operation(f"{l}{dashesP[count]}${m}{line}")
        count += 1
    count = 0
    operation(f"GRAND TOTAL{line}")
    operation(f"${round(sum(storetotal.values()))}\n")

#loop to rerun the code for all locations
while True:
    storesum.clear()
    q = input("Would you like to add a store? y/n\n").lower()
    if q == "y" or q == "":
        store = input("What is the name of this store?: ")
        if len(store) >= 29:
            print("Please enter a shorter store name!")
            continue
        #below is code to remove the amount of dashes in the dashes list to even out all the totals for looks
        for i in range(len(store)):
            dashes.pop(i)
        dashesP.append("".join(dashes))
        for _ in store:
            dashes.append("-")
        bills(store)
    elif q == "n":
        totals(print,"")
        save = input("Would you like to save this data? y/n\n")
        if save == "y" or save == "":
            with open("IncomeLogs.txt","w") as logs:
                logs.write(str(totals(logs.write,"\n")))
                exit()
        else:
            exit("Thanks!")
    else:
        print("Please enter y/n!")