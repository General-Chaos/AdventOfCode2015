import os
import re

fileDir = os.path.dirname(os.path.realpath(__file__))
moleculeinput = os.path.join(fileDir, 'molecule.txt')
probleminput = os.path.join(fileDir, 'input.txt')

molecule = open(moleculeinput).read()

substitutions = []
for line in open(probleminput):
    m = re.search(r"(\w+) => (\w+)", line)
    substitutions.append([m.group(1), m.group(2)])

Answer1 = 0
results = set()
for sub in substitutions:
    c = re.finditer(sub[0], molecule)
    for d in c:
        if d:
            replacedstring = molecule[:(d.start())] + sub[1] + molecule[(d.end()):]
            results.add(replacedstring)

Answer1 = len(results)
print(f"The answer to 1 is: {Answer1}")
