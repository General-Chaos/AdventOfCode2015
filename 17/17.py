litres = 150
containers = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]


def getcontainers(length, containers, passedlist=[]):
    newcontainers = containers.copy()
    newlist = passedlist.copy()
    container = newcontainers[0]
    if container > length:
        if len(newcontainers) > 1:
            yield from getcontainers(length, newcontainers[1:], newlist)
    elif container == length:
        yieldlist = passedlist.copy()
        yieldlist.append(container)
        yield yieldlist
        if len(newcontainers) > 1:
            yield from getcontainers(length, newcontainers[1:], newlist)
    elif len(newcontainers) > 1:
        yield from getcontainers(length, newcontainers[1:], newlist)
        newlist.append(container)
        yield from getcontainers((length - container), newcontainers[1:], newlist)
    else:
        pass

allcombos = list(getcontainers(150, containers))

print(f"Answer 1 is: {len(allcombos)}")

min = min(map(len, allcombos))
count = 0 
for i in allcombos:
    if len(i) == min:
        count += 1
print(f"Answer 2 is: {count}")
