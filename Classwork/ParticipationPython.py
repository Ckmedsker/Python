names = []
prices = []
total = 0
average = 0

q = "y"
while q == "y" or q == "":
    names.append(input("What is one friend's name?\n"))
    prices.append(int(input(("What is the price of their food?\n"))))
    while True:
        q = input("Add another person?: ")
        if q == "y" or q == "" or q == "n":
            break
        else:
            continue

k = len(prices)
for h in prices:
    total = total + h

average = total / k
print(f"The total cost is {total}, and the average per person is {average}.")

for i, j in zip(names, prices):
    if j > average:
        print(f"{i}'s price is ${j - average} less than the average!")
    elif j < average:
        print(f"{i}'s price is ${average - j} greater than the average!")
