import os
import mod23

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')

with open(probleminput) as f:
    problemdata = [line.rstrip('\n') for line in f.readlines()]

result1 = None
for result1 in mod23.InstructionSet(0, 0, problemdata):
    pass

print(f"The Answer to part 1 is: {result1[1]}")

result2 = None
for result2 in mod23.InstructionSet(1, 0, problemdata):
    pass

print(f"The Answer to part 2 is: {result2[1]}")
