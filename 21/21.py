from mod21 import *
from itertools import combinations

# for the weapons the permutations are just the list
weapons = (
    Equipment('Dagger', 8, 4, 0),
    Equipment('Shortsword', 10, 5, 0),
    Equipment('Warhammer', 25, 6, 0),
    Equipment('Longsword', 40, 7, 0),
    Equipment('Greataxe', 74, 8, 0)
)

# For armour we just need a No armour option
armour = (
    Equipment('NoArmour', 0, 0, 0),
    Equipment('Leather', 13, 0, 1),
    Equipment('Chainmail', 31, 0, 2),
    Equipment('Splintmail', 53, 0, 3),
    Equipment('Bandedmail', 75, 0, 4),
    Equipment('Platemail', 102, 0, 5)
)

# For rings we have a no ring option and force a double no ring
ringchoices = (
    Equipment('NoRing', 0, 0, 0),
    Equipment('Damage1', 25, 1, 0),
    Equipment('Damage2', 50, 2, 0),
    Equipment('Damage3', 100, 3, 0),
    Equipment('Armour1', 20, 0, 1),
    Equipment('Armour2', 40, 0, 2),
    Equipment('Armour3', 80, 0, 3)
)

rings = list(combinations(ringchoices, 2))
rings.append((Equipment('NoRing', 0, 0, 0), Equipment('NoRing', 0, 0, 0)))

# Now we get all the possible combinations of weapons and create boss fights for all of them
winners = list()
losers = list()
iterations = 0
for i in weapons:
    for j in armour:
        for k in rings:
            name = f"Fighter{iterations}"
            equipment = (i, j, k[0], k[1])
            winner = fight(Fighter(name, 100, 0, 0, equipment), Fighter("BOSS", 100, 8, 2))
            if winner.name == name:
                winners.append(winner)
            else:
                losers.append(Fighter(name, 100, 0, 0, equipment))
            iterations += 1

# Find the cheapest winner for part 1
winners.sort(key=lambda x: x.goldspent)
print(f"The Answer to part 1 is: {winners[0].goldspent}")

# Find the most expensive loser for part 2
losers.sort(key=lambda x: x.goldspent, reverse=True)
print(f"The Answer to part 2 is: {losers[0].goldspent}")
