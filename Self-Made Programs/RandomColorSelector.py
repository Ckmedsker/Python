print("Welcome to Cam's Color Selector!")
print("Please do not enter any values under 0 or any values over 255!!")


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

text = ("This text was colored by YOU!")
r = int(input("What is the value you want for Red: "))
g = int(input("What is the value you want for Green: "))
b = int(input("What is the value you want for Blue: "))


print(f"RGB Values: \nRed:{r}|Green:{g}|Blue:{b}")
print(colored(r,g,b,text))