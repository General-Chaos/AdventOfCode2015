import os
import copy

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')

for line in open(probleminput):
    line = line.rstrip('\n')
    if not ('inputarray' in locals()):
        inputarray = []
        for j in line:
            inputarray.append([])
    for i, k in enumerate(line):
        if k == "#":
            inputarray[i].append(True)
        else:
            inputarray[i].append(False)


def iterate(array):
    newarray = copy.deepcopy(array)
    for i, item in enumerate(array):
        for j, subitem in enumerate(item):
            trues = 0
            falses = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if ((i + k) < 0) or ((i + k) > (len(array) - 1)):
                        currentitem = False
                    elif ((j + l) < 0) or ((j + l) > (len(item) - 1)):
                        currentitem = False
                    else:
                        currentitem = array[(i + k)][(j + l)]
                    if (k == 0) and (l == 0):
                        pass
                    elif currentitem:
                        trues += 1
                    else:
                        falses += 1
            if subitem and (trues not in (2, 3)):
                newarray[i][j] = False
            elif (not subitem) and (trues == 3):
                newarray[i][j] = True
    return newarray

for i in range(100):
    inputarray = iterate(inputarray)
trues = 0

for i in inputarray:
    for j in i:
        if j:
            trues += 1

print(f"Answer 1 is: {trues}")


def setcorners(array):
    for i in range(-1, 1):
        for j in range(-1, 1):
            array[i][j] = True

for line in open(probleminput):
    line = line.rstrip('\n')
    if not ('inputarray2' in locals()):
        inputarray2 = []
        for j in line:
            inputarray2.append([])
    for i, k in enumerate(line):
        if k == "#":
            inputarray2[i].append(True)
        else:
            inputarray2[i].append(False)

setcorners(inputarray2)

for i in range(100):
    inputarray2 = iterate(inputarray2)
    setcorners(inputarray2)

trues = 0
for i in inputarray2:
    for j in i:
        if j:
            trues += 1

print(f"Answer 2 is: {trues}")
