import random
import os

print("Welcome to Cam's Quiz. Please enter 1, 2, 3, or 4 for each input")
questions = ["Who is the current instructor? ","What is the 7th letter of the alphabet? (I can hear you singing) ","Which corner is Sydney in? ",
             "Who DOESN'T come to class earlier? ","What movie is in space? ","What is the most evil gaming company? ",
             "What question number is this?","Why does Joe keep calling Amos Jon?","How do you spell this word? ",
             "What does song goes like: Never gonna give you up, never gonna let you down, never gonna turn around, and desert you? "]
Q1 = ["Michael","Joe","Amos","Tux"]
Q2 = ["G","F","H","I"]
Q3 = ["Leftside of you, on the green wall","Rightside of you, on the green wall","Leftside of you, on the white wall","Rightside of you, on the white wall"]
Q4 = ["Ok this is just a freebie","Cam","Amos","Jon"]
Q5 = ["Star Wars","Space Wars","Cars","Shrek"]
Q6 = ["Nintendo","Epic Games","Xbox","Sony"]
Q7 = ["7","6","8","9"]
Q8 = ["I'm not really sure I think Joe is definitely not meaning to","Joe doesn't know Amos' name","Amos and Jon looked too similar","They actually switched seats at one point"]
Q9 = ["Atrocious","Atricious","I actually mispelled the word at first too haha","Atricitrus"]
Q10 = ["Never gonna give you up","Rick Astley","Never gonna let you down","you just got rickrolled and you freaking know it"]

Q = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10]
count = 0
count2 = 0
score = 0
answer = 0

for i in Q:
    random.shuffle(Q[count])
    print(Q[count])
    element1 = Q[count].index(Q[count][count2])
    element2 = Q[count].index(Q[count][count2 + 1])
    element3 = Q[count].index(Q[count][count2 + 2])
    element4 = Q[count].index(Q[count][count2 + 3])
    element = [element1, element2, element3, element4]
    print(element)
    print(element1)
    """for i in element:
        if element[count][count2] == 0:
            answer = 0
        elif element[count + 0][count2] == 1 or 2 or 3:
            answer = 1"""
    count2 = 0
    print(f"{questions[0 + count]}\n{Q[0 + count][0]}\n{Q[0 + count][1]}\n{Q[0 + count][2]}\n{Q[0 + count][3]}")
    userInput = int(input("\nWhat is the answer?\n"))
    if userInput == 1:
        userInput = 0
    elif userInput == 2:
        userInput = 1
    elif userInput == 3:
        userInput = 2
    elif userInput == 4:
        userInput = 3
    if userInput == element1:
        print("Correct\n")
        score = score + 1
    else:
        print("Incorrect")
    count = count + 1
score = score * 10
if score < 60:
    print(f"You failed! Your score is: {score}%.")
elif score == 60:
    print(f"You got a D! Your score is:{score}%.")
elif score == 70:
    print(f"You got a C! Your score is:{score}%.")
elif score == 80:
    print(f"You got a B! Your score is:{score}%.")
elif score == 90:
    print(f"You got a A! Your score is:{score}%.")
elif score == 100:
    print(f"You got a perfect score! Your score is:{score}%.")