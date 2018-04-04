import json
import os
import re

fileDir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(fileDir, 'input.json')
# json = open(filename).read()

# for the first part just ignore the json and regex out the numbers
# this requires the input to be formatted into "neat" json. I used vscode
answer1 = 0
for line in open(filename):
    m = re.search(r"(\-?\d+)", line)
    if m:
        answer1 += int(m.group())

print(f"Answer 1 is: {answer1}")

# Part 2, actually interprit the json
jsonobject = json.loads(open(filename).read())

answer2 = 0


def iteratered(randobj):
    global answer2
    if type(randobj) is str:
        pass
    elif type(randobj) is int:
        answer2 += randobj
    elif type(randobj) is list:
        for rand in randobj:
            iteratered(rand)
    elif type(randobj) is dict:
        if "red" in randobj.values():
            pass
        else:
            for rand in randobj.values():
                iteratered(rand)

iteratered(jsonobject)

print(f"Answer 2 is: {answer2}")
