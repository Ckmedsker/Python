#(tuple) unmuted
#[list] mutable
#{dictonary} definable
#dictonaries have keys and values
#keys are first, and values are second

letter_grades = {"A":4.0, "B":3.0, "C":2, "D":1}
letter_grades["F"] = 0
print(letter_grades)
letter_grades.update({"A":4, "B":3, "C":2, "D":1, "F":0})
print(letter_grades)
print(letter_grades.keys())
for i in (letter_grades.keys()):
    print(i)

print(letter_grades.values())
for i in letter_grades.values():
    print(i)

print(letter_grades.items())
for i,j in letter_grades.items():
    print(i,j)

print(letter_grades["A"])

def get_key(arg, dictionary):
    for key, value in dictionary.items():
        if key == arg:
            return key

x = get_key(2.0,letter_grades)


grades = ["A","B","A","F", "D", "A", "F", "A", "A", "C", "C", "B"]
count = {}
for i in grades:
    count[i] = count.get(i,0) + 1
print(count)