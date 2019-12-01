from input2 import values
import re

steps = values().split("\n")

for x in range(0, len(steps)):
    steps[x] = steps[x].strip()

masterIndex = { }
required = []
stepsKeys = []
completed = []
result = ""
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for x in range(0, len(steps)):
    name = re.search("step..", steps[x]).group(0)[5:6]
    require = re.match("Step..", steps[x]).group(0)[5:6]

    if name not in stepsKeys:
        if require not in required:
            required.append(require)
        stepsKeys.append(name)
    else:
        if require not in required:
            required.append(require)

    try:
        masterIndex[name].append(require)
    except:
        masterIndex[name] = [require]

possibles = []

for x in range(0, len(required)):
    test = required[x]
    if test not in stepsKeys:
        result = test
        possibles.append(test)

excluded = len(possibles)
testing = False
for x in range(0, len(alpha)):
    if alpha[x] in possibles and testing == False:
        result = alpha[x]
        testing = True
        possibles.remove(alpha[x])
        completed.append(alpha[x])

while len(result) != len(masterIndex) + excluded:
    for x in range(0, len(stepsKeys)):
        if stepsKeys[x] not in possibles:
            try:
                result.index(stepsKeys[x])
            except:
                test = masterIndex[stepsKeys[x]]
                no = True
                for p in range(0, len(test)):
                    if test[p] not in completed:
                        no = False
                    elif no == True and p + 1 == len(test):
                        possibles.append(stepsKeys[x])

    testing = False
    for x in range(0, len(alpha)):
        if alpha[x] in possibles and testing == False:
            result =  result + alpha[x]
            testing = True
            possibles.remove(alpha[x])
            completed.append(alpha[x])

print(result)
    