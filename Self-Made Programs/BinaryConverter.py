print("Hello Welcome to Cam's Binary Converter!")
print("First you must enter a binary number in regular format! (syntax:0000)\n")
reg = int(input("What is your binary number in regular format?: "))
#if int(reg) < 1 or int(reg) > 0:
    #print("Please enter an integer between 0 or 1!")
    #sys.exit()
firList = list(str(reg))
secList = []
print("")
print("This is regular binary written in 1st compliment: " + str(firList))

count = -1
#print(firList[count] and type(firList[count]))
count2 = -1
for i in firList:
    firList[count] = int(firList[count2])
    count2 = count2 + 1
print()
while True:
    if type(firList) != int:
        firList[count] = int(firList[count2])
    else:
        print(type(firList))
        if firList[count] == 0:
            firList[count] = 1
            break
        elif firList[count] == 1:
            count = count - 1
        else:
            break

print(firList)