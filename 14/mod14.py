import re


class Reindeer:

    distancedict = {}

    def __init__(self, inputstring):
        pattern = r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
        m = re.search(pattern, inputstring)
        self.__name = m.group(1)
        self.__speed = int(m.group(2))
        self.__flightduration = int(m.group(3))
        self.__restduration = int(m.group(4))
        self.__state = 'flying'
        self.__distance = 0
        self.__flighttime = 0
        self.__resttime = 0
        self.__score = 0
        Reindeer.distancedict.update({self.__name: self.__distance})

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
        raise OverflowError("You cannot set the distance!")

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        raise OverflowError("You cannot set the distance!")

    def iterate(self):
        if self.__state == 'flying':
            self.__distance += self.__speed
            Reindeer.distancedict.update({self.__name: self.__distance})
            self.__flighttime += 1
            if self.__flighttime == self.__flightduration:
                self.__state = 'resting'
                self.__flighttime = 0
        else:
            self.__resttime += 1
            if self.__resttime == self.__restduration:
                self.__state = 'flying'
                self.__resttime = 0

    def updatescore(self):
        if self.__distance == max(Reindeer.distancedict.values()):
            self.__score += 1

    def __str__(self):
        return f"Reindeer: {self.__name} Distance: {self.__distance} Score: {self.__score}"

if __name__ == '__main__':
    test = Reindeer("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.")
    for i in range(1000):
        test.iterate()
        test.updatescore()
    print(test)
