import random
import sys
#I imported sys to exit the program when needed

print("Welcome to Cam's Number Guessing Game!")
print("You will have 5 tries to guess a number 1 through 100!")
print("The game will tell you whether you need to guess higher or lower!\n")

def playGame():
    rand = random.randrange(1,100)
    for i in range(5):
        guess = int(input("Please enter a number!"))
        if guess > 100 or guess < 1:
            print("Next time enter a number within the range!")
            return exit()
        if guess == rand:
            print("Congrats!!! You guessed the number correctly!")
            return
        elif guess <= rand:
            print("Your guess is too low! Please guess higher.")
        elif guess >= rand:
            print("Your guess is too high! Please guess lower.")
    if guess != rand:
        print("You lose, loser...")
playGame()

while True:
    playAgain = str(input("Do you want to play again?: Y|n\n"))
    print(playAgain)
    if playAgain == "Y":
        playGame()
    else:
        print("Thank you for playing!")
        sys.exit()