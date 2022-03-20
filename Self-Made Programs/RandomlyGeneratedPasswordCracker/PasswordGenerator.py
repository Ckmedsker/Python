import random
import string


def randomPassword(length):
    printable = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join((random.choice(printable) for i in range(length)))
    print("Random alphanumeric String is:", result_str)
    return result_str