import os
import mod15

ingredients = []
fileDir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(fileDir, 'input.txt')
for line in open(filename):
    ingredients.append(mod15.Ingredient(line))

scores = []

for i in mod15.get_partitioncounts(100, 4):
    cookie = mod15.Cookie()
    for j, k in enumerate(i):
        if k == 0:
            pass
        else:
            cookie.add_ingredient(ingredients[j], k)
    scores.append(cookie.get_score())

print(f"Answer to part 1: {max(scores)}")

# Part 2 only includes cookies with a score of 500

scores = []
for i in mod15.get_partitioncounts(100, 4):
    cookie = mod15.Cookie()
    for j, k in enumerate(i):
        if k == 0:
            pass
        else:
            cookie.add_ingredient(ingredients[j], k)
    if cookie.get_calories() == 500:
        scores.append(cookie.get_score())
    else:
        pass

print(f"Answer to part 2: {max(scores)}")
