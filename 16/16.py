import os
import re

fileDir = os.path.dirname(os.path.realpath(__file__))
mfcsaminput = os.path.join(fileDir, 'MFCSAM.txt')
probleminput = os.path.join(fileDir, 'input.txt')

# import the MFCSCAN input into a dict
alphasue = {}
for line in open(mfcsaminput):
    m = re.search(r"(\w+): (\d+)", line)
    alphasue.update({m.group(1): int(m.group(2))})

# import each sue into a sue dictionary
# assume any unknown values are equal to the MFC output
alphasuekeys = list(alphasue.keys())
sues = {}
for line in open(probleminput):
    sue = re.search(r"^(\w+ \d+):", line,)
    sues.update({sue.group(1): {}})
    m = re.findall(r"((\w+): (\d+))", line)
    for n in m:
        sues[sue.group(1)].update({n[1]: int(n[2])})
    for key in alphasuekeys:
        if key not in sues[sue.group(1)].keys():
            sues[sue.group(1)].update({key: alphasue[key]})

# Find the matching dictionary for part 1
for sue in sues:
    if sues[sue] == alphasue:
        print(f"The answer to part 1 is: {sue}")

sues = {}
# For part 2 do the same but do comparisons
# If comparison is false put a non matching string in
for line in open(probleminput):
    sue = re.search(r"^(\w+ \d+):", line,)
    sues.update({sue.group(1): {}})
    m = re.findall(r"((\w+): (\d+))", line)
    for n in m:
        if n[1] in ('cats', 'trees'):
            if int(n[2]) > alphasue[n[1]]:
                sues[sue.group(1)].update({n[1]: alphasue[n[1]]})
            else:
                sues[sue.group(1)].update({n[1]: 'NotAMatch'})
        elif n[1] in ('pomeranians', 'goldfish'):
            if int(n[2]) < alphasue[n[1]]:
                sues[sue.group(1)].update({n[1]: alphasue[n[1]]})
            else:
                sues[sue.group(1)].update({n[1]: 'NotAMatch'})
        else:
            sues[sue.group(1)].update({n[1]: int(n[2])})
    for key in alphasuekeys:
        if key not in sues[sue.group(1)].keys():
            sues[sue.group(1)].update({key: alphasue[key]})

# Find the matching dictionary for part 2
for sue in sues:
    if sues[sue] == alphasue:
        print(f"The answer to part 2 is: {sue}")
