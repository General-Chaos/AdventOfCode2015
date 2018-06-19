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
