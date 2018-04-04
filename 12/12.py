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

print(f"Answer 1 is:{answer1}")

# Part 2, actually interprit the json
jsonobject = json.loads(open(filename).read())
for a in jsonobject:
    print(a)

print('red' in jsonobject.values())
