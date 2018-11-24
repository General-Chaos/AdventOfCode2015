import mod22
import copy

mage = mod22.Mage("mage", 50, 0, 0, 500)
boss = mod22.Fighter("boss", 71, 10, 0)

bestmana = 99999999
victories = list(mod22.get_victorious_mage_fights(mage, boss, bestmana))
victories.sort(key=lambda x: x.manaspent)
print(f"The Answer to part 1 is: {victories[0].manaspent}")

bestmana = 99999999
victories = list(mod22.get_victorious_mage_fights(mage, boss, bestmana, 'Hard'))
victories.sort(key=lambda x: x.manaspent)
print(f"The Answer to part 2 is: {victories[0].manaspent}")
