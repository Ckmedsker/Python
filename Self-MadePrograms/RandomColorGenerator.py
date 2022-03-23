import random
import time

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    text = (f"This color is randomly generated!: RGB Values: \nRed:{r}|Green:{g}|Blue:{b}")
    print(colored(r,g,b, text))
    time.sleep(0.01)