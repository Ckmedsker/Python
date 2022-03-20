import random

rand = random.randint(0,1702)
print("Welcome to Cam's Hangman o-</(!\n")
stages = [("  |----|\n  |   _|_\n  |\n  |\n  |\n__|__"),
("  |----|\n  |   _|_\n  |    0\n  |\n  |\n__|__"),
("  |----|\n  |   _|_\n  |    0\n  |    |\n  |\n__|__"),
("  |----|\n  |   _|_\n  |    0\n  |   /|\n  |\n__|__"),
("  |----|\n  |   _|_\n  |    0\n  |   /|\\\n  |\n__|__"),
("  |----|\n  |   _|_\n  |    0\n  |   /|\\\n  |   /\n__|__"),
("  |----|\n  |   _|_\n  |    0\n  |   /|\\\n  |   / \\\n__|__"),
("  |----|\n  |   _|_\n  |    0\n  |   /|\\\n  |   /*\\\n__|__")]
alp = list("abcdefghijklmnopqrstuvwxyz1234567890")
un = []
count = 0
numb = 0
incorrectA = 0
guesses = []

word1 = str(input("Enter a word to be guessed! Please don't use other characters than letters and numbers!: ")).lower()
word = list(word1)
print("")
for char in word1:
    un.append("_")
print(stages[0])
print(f"             {''.join(un)}")
print(f"Characters guessed:{guesses}")
while True:
    guess = input(f"What is your #{count + 1} guess?: ")
    if guess in(list(word1)):
        guesses.append(guess)
        un[] = guess


#if guess ==