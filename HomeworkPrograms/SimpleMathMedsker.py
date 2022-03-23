numb1 = int(input("Enter a number!"))
numb2 = int(input("Enter a number!"))
if numb2 == 0:
    exit("Please enter a number other than 0!")
add = numb1 + numb2
sub = numb1 - numb2
multi = numb1 * numb2
divi = numb1 / numb2
print(str(numb1) + " + " + str(numb2) + " = " + str(add)
+ "|" + str(numb1) + " - " + str(numb2) + " = " + str(sub)
+ "|" + str(numb1) + " * " + str(numb2) + " = " + str(multi)
+ "|" + str(numb1) + " / " + str(numb2) + " = " + str(divi))