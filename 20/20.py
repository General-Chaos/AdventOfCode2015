import itertools


# First attempt i brute forced all factors but it took far too long
# So I looked up the formula to calcuate the sum from the prime factors
def get_primefactors(number):
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            yield i
    if number > 1:
        yield number


def get_scores():
    i = 1
    while True:
        score = 1
        primegroup = itertools.groupby((get_primefactors(i)))
        for j in primegroup:
            multiplier = (((j[0] ** (len(list(j[1])) + 1)) - 1) / (j[0] - 1))
            score = score * multiplier
        yield (i, (score * 10))
        i = i + 1

for i in get_scores():
    if i[1] < 29000000:
        pass
    else:
        print(f"The answer to 1 is: {i[0]}")
        break


# For part 2 we need to actually get the factors and discard any scores from factors below i/50
def get_uniquefactors(number):
    primefactors = list(get_primefactors(number))
    uniquefactors = set()
    for i in range(len(primefactors) + 1):
        for j in itertools.combinations(primefactors, i):
            r = 1
            for k in j:
                r *= k
            uniquefactors.add(r)
    return uniquefactors


def get_scores_2():
    i = 1
    while True:
        base = i / 50
        score = 0
        for j in get_uniquefactors(i):
            if j >= base:
                score += (j * 11)
        yield (i, score)
        i += 1


for i in get_scores_2():
    if i[1] < 29000000:
        pass
    else:
        print(f"The answer to 2 is: {i[0]}")
        break
