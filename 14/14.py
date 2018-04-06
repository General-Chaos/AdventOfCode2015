import os
from mod14 import Reindeer

# load the input and create the list of reindeer objects
fileDir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(fileDir, 'input.txt')
reindeerlist = []
for line in open(filename):
    reindeerlist.append(Reindeer(line))

# Part 1/2 iterate the reindeer by the requested seconds
# Update the distance travelled and score if they are winning
part1_seconds = 2503

for i in range(part1_seconds):
    for deer in reindeerlist:
        deer.iterate()
    for deer in reindeerlist:
        deer.updatescore()

winner1 = sorted(reindeerlist, key=lambda x: x.distance, reverse=True)[0]
print(f"Winner of part 1 is: {str(winner1)}")

winner2 = sorted(reindeerlist, key=lambda x: x.score, reverse=True)[0]
print(f"Winner of part 2 is: {str(winner2)}")
