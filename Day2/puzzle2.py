import input

listValues = input.values().split("\n")
commonLetter = ""

for x in range(0, len(listValues)):
    testString = list(listValues[x])

    for y in range(0, len(listValues)):
        if (listValues[y] != listValues[x]):
            booleans = []
            for z in range(0, len(testString)):
                if(testString[z] == list(listValues[y])[z]):
                    booleans.append(True)
                else:
                    booleans.append(False)
            
            if(booleans.count(False) == 1 and commonLetter == ""):
                commonLetter = listValues[x].replace(testString[booleans.index(False)], "")

print("Your answer is...\n" + commonLetter)