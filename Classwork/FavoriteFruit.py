FavF = []
count = 0

q1 = int(input("How many favorite fruits do you have?: "))
while q1 != count:
    FavF.append(input("Please enter one of your favorite fruits? "))
    count = count + 1
for i in FavF:
    print("One of you favorite fruits is " + i)

