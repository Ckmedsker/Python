import hashlib
from PasswordGenerator import randomPassword

def passwordFile():
    x = randomPassword(4)
    hashed = hashlib.md5(x.encode("UTF-8")).hexdigest()
    with open("shadow2.txt","w") as file:
        file.write(f"{hashed}\n")