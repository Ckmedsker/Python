#generate a brute force password list to read off the 1mil most common password. Compare the passwords, and the input
#This is called a dictionary attack

import hashlib
import string
import itertools
import hashed


with open("shadow.txt","r") as fShadow:
    with open("pass_list.txt","r") as pass_list:
        for line in fShadow:
            for passwd in pass_list:
                hashed = hashlib.md5(passwd[:-1].encode("UTF-8")).hexdigest()
                if line[:-1] == hashed:
                    print(f"\n\nCracked\n\n{hashed}    {passwd}\n\nThe password is {passwd}")

count = 1
hashed.md5hasher()
with open("shadow.txt", "r") as fShadow:
    with open("pass_list.txt", "r") as wordList:
        for line in fShadow:
            for i in wordList:
                comma = ("{:,}".format(count))
                hashed = hashlib.md5(i[:-1].encode("UTF-8")).hexdigest()
                print(f"{hashed}    {comma}) {i[:-1]}")
                count += 1
                if hashed == line[:-1]:
                    print(f"\n\nCRACKED\n\n{hashed}    {i[:-1]}\n\nThe password is {i[:-1]}")
                    quit()