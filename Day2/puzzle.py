import input

listValues = input.values().split("\n")

twice = 0
three = 0

for x in range(0, len(listValues)):
    letters = list(listValues[x])

    uniqueLetter = { }
    two = False
    third = False

    for y in range(0, len(letters)):
        if(uniqueLetter.get(letters[y]) == None):
            uniqueLetter[letters[y]] = 1
        else:
            if(uniqueLetter.get(letters[y]) == 1):
                uniqueLetter[letters[y]] = 2
            elif(uniqueLetter.get(letters[y]) == 2):
                uniqueLetter[letters[y]] = 3
            elif(uniqueLetter.get(letters[y]) == 3):
                uniqueLetter[letters[y]] = 4

    uniqueLetterKey = list(dict.values(uniqueLetter))

    for y in range(0, len(uniqueLetterKey)):
        if (uniqueLetterKey[y] == 2 and two == False):
            two = True
            twice = twice + 1
        elif(uniqueLetterKey[y] == 3 and third == False):
            third = True
            three = three + 1

print("Your answer is...")
print(twice * three)