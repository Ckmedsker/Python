import random

#im such a silly person, I am mad the code is so long, I thought of a much more efficient way after I finished it. I will probably turn it better later haha.
print("Welcome to Cam's Quiz. Please enter 0,1,2, or 3 for each input")
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

count = 0
score = 0

random.shuffle(Q1)
element1 = Q1.index("Michael")
element2 = Q1.index("Joe")
element3 = Q1.index("Amos")
element4 = Q1.index("Tux")
print(f"{questions[0 + count]}\n")
print(Q1[0])
print(Q1[1])
print(Q1[2])
print(Q1[3])
userinput = int(input("\nWhat is the answer?\n"))
if userinput == element1:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")
count = count + 1
random.shuffle(Q2)
element1 = Q2.index("G")
element2 = Q2.index("F")
element3 = Q2.index("H")
element4 = Q2.index("I")
print(f"{questions[0 + count]}\n")
print(Q2[0])
print(Q2[1])
print(Q2[2])
print(Q2[3])
userinput = int(input("\nWhat is the answer?\n"))
if userinput == element1:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")
count = count + 1
random.shuffle(Q3)
element1 = Q3.index("Leftside of you, on the green wall")
element2 = Q3.index("Rightside of you, on the green wall")
element3 = Q3.index("Leftside of you, on the white wall")
element4 = Q3.index("Rightside of you, on the white wall")
print(f"{questions[0 + count]}\n")
print(Q3[0])
print(Q3[1])
print(Q3[2])
print(Q3[3])
userinput = int(input("\nWhat is the answer?\n"))
if userinput == element1:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")
count = count + 1
random.shuffle(Q4)
element1 = Q4.index("Ok this is just a freebie")
element2 = Q4.index("Amos")
element3 = Q4.index("Jon")
element4 = Q4.index("Cam")
print(element1,element2,element3,element4)
print(f"{questions[0 + count]}\n")
print(Q4[0])
print(Q4[1])
print(Q4[2])
print(Q4[3])
userinput = int(input("\nWhat is the answer?\n"))
if userinput == element1:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")
count = count + 1
random.shuffle(Q5)
element1 = Q5.index("Star Wars")
element2 = Q5.index("Space Wars")
element3 = Q5.index("Cars")
element4 = Q5.index("Shrek")
print(f"{questions[0 + count]}\n")
print(Q5[0])
print(Q5[1])
print(Q5[2])
print(Q5[3])
userinput = int(input("\nWhat is the answer?\n"))
if userinput == element1:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")
count = count + 1
random.shuffle(Q6)
element1 = Q6.index("Nintendo")
element2 = Q6.index("Epic Games")
element3 = Q6.index("Xbox")
element4 = Q6.index("Sony")
print(f"{questions[0 + count]}\n")
print(Q6[0])
print(Q6[1])
print(Q6[2])
print(Q6[3])
userinput = int(input("\nWhat is the answer?\n"))
if userinput == element1:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")
count = count + 1
random.shuffle(Q7)
element1 = Q7.index("7")
element2 = Q7.index("6")
element3 = Q7.index("8")
element4 = Q7.index("9")
print(f"{questions[0 + count]}\n")
print(Q7[0])
print(Q7[1])
print(Q7[2])
print(Q7[3])
userinput = int(input("\nWhat is the answer?\n"))
if userinput == element1:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")
count = count + 1
random.shuffle(Q8)
element1 = Q8.index("I'm not really sure I think Joe is definitely not meaning to")
element2 = Q8.index("Amos and Jon looked too similar")
element3 = Q8.index("They actually switched seats at one point")
element4 = Q8.index("Joe doesn't know Amos' name")
print(f"{questions[0 + count]}\n")
print(Q8[0])
print(Q8[1])
print(Q8[2])
print(Q8[3])
userinput = int(input("\nWhat is the answer?\n"))
if userinput == element1:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")
count = count + 1
random.shuffle(Q9)
element1 = Q9.index("Atrocious")
element2 = Q9.index("Atricious")
element3 = Q9.index("I actually mispelled the word at first too haha")
element4 = Q9.index("Atricitrus")
print(f"{questions[0 + count]}\n")
print(Q9[0])
print(Q9[1])
print(Q9[2])
print(Q9[3])
userinput = int(input("\nWhat is the answer?\n"))
if userinput == element1:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")
count = count + 1
random.shuffle(Q10)
element1 = Q10.index("Never gonna give you up")
element2 = Q10.index("Rick Astley")
element3 = Q10.index("Never gonna let you down")
element4 = Q10.index("you just got rickrolled and you freaking know it")
print(f"{questions[0 + count]}\n")
print(Q10[0])
print(Q10[1])
print(Q10[2])
print(Q10[3])
userinput = int(input("\nWhat is the answer?\n"))
if userinput == element1:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

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