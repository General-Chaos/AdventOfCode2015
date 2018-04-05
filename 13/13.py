import os
import re
import itertools

fileDir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(fileDir, 'input.txt')
hatemap = {}
pattern = r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)."

# convert file into a searchable dictionary of hate
for line in open(filename):
    m = re.search(pattern, line)
    if m.group(1) not in hatemap.keys():
        hatemap.update({m.group(1): {}})
    if m.group(2) == 'lose':
        amount = -1 * int(m.group(3))
    else:
        amount = int(m.group(3))
    hatemap[m.group(1)].update({m.group(4): amount})

# define how to calculate the hate at the table


def calculatehate(iteration):
    hate = 0
    for i in range(len(iteration)):
        prev = i - 1
        if i == (len(iteration) - 1):
            next = 0
        else:
            next = i + 1
        hate += hatemap[iteration[i]][iteration[prev]]
        hate += hatemap[iteration[i]][iteration[next]]
    return hate


# iterate over all the permutations using standard itertools function
answer1 = max(list(map(calculatehate, itertools.permutations(hatemap.keys()))))
print(f"Answer 1 is: {answer1}")

# part2
# get current keys and then add myself and pure ambivalence
currkeys = set(hatemap.keys())
hatemap.update({"GeneralChaos": {}})
for key in currkeys:
    hatemap[key].update({"GeneralChaos": 0})
    hatemap["GeneralChaos"].update({key: 0})

# get the min hate of the new iterations
answer2 = max(list(map(calculatehate, itertools.permutations(hatemap.keys()))))
print(f"Answer 2 is: {answer2}")
