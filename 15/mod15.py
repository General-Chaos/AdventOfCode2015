import re
from itertools import islice


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


class Ingredient:

    def __init__(self, string):
        pattern = r"(\w+): (\w+) (-?\d+), (\w+) (-?\d+), (\w+) (-?\d+), (\w+) (-?\d+), (\w+) (-?\d+)"
        m = re.search(pattern, string)
        self.__name = m.group(1)
        self.__attributes = {}
        for group in chunk(m.groups()[1:], 2):
            if group[0] == 'calories':
                self.__calories = int(group[1])
            else:
                self.__attributes.update({group[0]: int(group[1])})

    def get_attributes(self):
        return self.__attributes

    def get_calories(self):
        return self.__calories

    def get_score(self, amount):
        score = {}
        for key in self.get_attributes():
            score.update({key: (self.get_attributes()[key] * amount)})
        return score

    def get_totalcalories(self, amount):
        return self.get_calories() * amount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        raise AttributeError("You cannot override the name!")


class Cookie:

    def __init__(self):
        self.__ingredients = []

    def add_ingredient(self, ingredient, amount):
        self.__ingredients.append((ingredient, amount))

    def get_score(self):
        scorekeeper = {}
        for ingredient in self.__ingredients:
            subscore = ingredient[0].get_score(ingredient[1])
            for key in subscore:
                if key in scorekeeper.keys():
                    scorekeeper[key] += subscore[key]
                else:
                    scorekeeper.update({key: subscore[key]})
        score = 1
        for key in scorekeeper:
            if scorekeeper[key] < 0:
                score *= 0
            else:
                score *= scorekeeper[key]
        return score

    def get_calories(self):
        calories = 0
        for ingredient in self.__ingredients:
            calories += ingredient[0].get_totalcalories(ingredient[1])
        return calories


def get_partitioncounts(number, partitions, passedlist=[]):
    if partitions == 1:
            passedlist.append(number)
            yield passedlist
    else:
        for i in range(number + 1):
            newlist = passedlist.copy()
            newlist.append(i)
            yield from get_partitioncounts((number - i), (partitions - 1), newlist)


if __name__ == "__main__":
    test = Ingredient("Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3")
    print(test.get_attributes())
    print(test.name)
    print(test.get_score(44))
    testcookie = Cookie()
    testcookie.add_ingredient(test, 44)
    print(testcookie.get_score())
    print(len(list(get_partitioncounts(100, 4))))
    print(testcookie.get_calories())
