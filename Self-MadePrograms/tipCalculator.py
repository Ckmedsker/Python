print("Welcome to Cam's Tip Calculator!")
meal = float(input("Please enter the price of your meal! $"))
percent = float(input("Please input what percent you would like to tip!: ")) / 100
calc = round(meal * percent,2)
total = meal + calc
print(f"Your tip is ${calc} with a {round(percent,2)}% tip, and your total is ${round(total,2)}!")