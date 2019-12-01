from input2 import values
import re

def letterCheck(letter, completed, masterIndex):
    test = masterIndex[letter]
    no = True
    for p in range(0, len(test)):
        if test[p] not in completed:
            no = False

    return no

steps = values().split("\n")

for x in range(0, len(steps)):
    steps[x] = steps[x].strip()

masterIndex = { }
required = []
stepsKeys = []
completed = []
result = ""
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
workers = { "0": [None, 0], "1": [None, 0] } #, "3": [None, 0], "4": [None, 0], "5": [None, 0] }
lenWork = 2

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

keys = list(result)

cont = False
completed.clear()

time = 0
x = 0
freeWork = 0
while cont is False:
    if len(keys) > 0:
        if keys[0] not in stepsKeys:
            workers[str(freeWork)] = [keys[0], alpha.index(keys[0]) + 1]
            keys.pop(0)
            freeWork = freeWork + 1
        else:
            for x in range(0, len(keys)):
                try:
                    check = letterCheck(keys[x], completed, masterIndex)
                
                    if check is True:
                        if freeWork < lenWork:
                            workers[str(freeWork)] = [keys[0], alpha.index(keys[0]) + 1]
                            keys.pop(0)
                            freeWork = freeWork + 1
                except:
                    x = 6

    print(workers)
    print(completed)
    print(freeWork)
    for y in range(0, len(workers)):
        if workers[str(y)][0] != None:
            workers[str(y)][1] = workers[str(y)][1] - 1

            if workers[str(y)][1] == 0 and workers[str(y)][0] != None:
                completed.append(workers[str(y)][0])
                workers[str(y)][0] = None
                freeWork = freeWork - 1

    time = time + 1

    no = False
    for y in range(0, len(workers)):
        if workers[str(y)][0] != None:
            no = True
        elif y == len(workers) and no == False:
            if len(keys) == 0:
                cont = True

print(completed)

print(result)
print(time)

print(time + (60 * len(result)))
    