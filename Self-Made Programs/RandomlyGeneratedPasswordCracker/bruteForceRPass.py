import hashlib
import string
import itertools

from hashedretry import passwordFile

passwordFile()
with open("shadow2.txt","r") as fShadow:
    for line in fShadow:
        for x in range(1,25):
            res = itertools.product(string.printable[:-6], repeat=x)
            for i in res:
                hashed = hashlib.md5("".join(i).encode("UTF-8")).hexdigest()
                #print(f"{hashed}    {''.join(i)}")
                if hashed == line[:-1]:
                    print(f"\n\nPassword Cracked!!!\n\nThe password is {''.join(i)}!!!")
                    quit()
