def get_num(question):
    def decorator(func):
        def wrapper():
            while True:
                try:
                    num = int(input(question))
                    return func(num)
                except ValueError:
                    print("You don't do numbers often do you?")
        return wrapper
    return decorator

@get_num("Give me a positive number: ")
def get_positive(num):
    if num > 0:
        return num
    else:
        print("That is not a positive number!")
        return get_positive()

@get_num("Give me a negative number: ")
def get_negative(num):
    if num < 0:
        return num
    else:
        print("That is not a negative number!")
        return get_negative()

@get_num("Give me an even number: ")
def get_even(num):
    mod = num % 2
    if mod == 0:
        return num
    else:
        print("That is not a even number!")
        return get_even()

if __name__ == "__main__":
    def main():
        num = get_positive()
        print(f"Your number is {num}.")
        num = get_negative()
        print(f"Your number is {num}.")
        num = get_even()
        print(f"Your number is {num}.")
    main()

