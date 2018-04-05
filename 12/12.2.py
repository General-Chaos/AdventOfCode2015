import json
import os

fileDir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(fileDir, 'input.json')
jsonobject = json.loads(open(filename).read())


def generatorjsonint(randobj):
    if type(randobj) is str:
        pass
    elif type(randobj) is int:
        yield randobj
    elif type(randobj) is list:
        for rand in randobj:
            yield from generatorjsonint(rand)
    elif type(randobj) is dict:
        for rand in randobj.values():
            yield from generatorjsonint(rand)

answer1 = sum(generatorjsonint(jsonobject))
print(f"Answer 1 is: {answer1}")


def generatorjsonintnored(randobj):
    if type(randobj) is str:
        pass
    elif type(randobj) is int:
        yield randobj
    elif type(randobj) is list:
        for rand in randobj:
            yield from generatorjsonintnored(rand)
    elif type(randobj) is dict:
        if "red" in randobj.values():
            pass
        else:
            for rand in randobj.values():
                yield from generatorjsonintnored(rand)

answer2 = sum(generatorjsonintnored(jsonobject))
print(f"Answer 2 is: {answer2}")
