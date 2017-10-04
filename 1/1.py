file = open("S:/Prod/AdventOfCode/NicMc/AdventOfCode2015/1/input.txt","r")
inputs = list(file.read())
i = 0
for inpu in inputs:
    if inpu == ')':
        i = i-1
    else:
        i = i+1
print("The answer to part 1 is: {}".format(i))
i = 0
j = 1
for inpu in inputs:
    if inpu == ')':
        i = i-1
    else:
        i = i+1
    if i == -1:
        break
    j = j+1

print("The answer to part 1 is: {}".format(j))

