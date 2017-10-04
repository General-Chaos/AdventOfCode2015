file = open("S:/Prod/AdventOfCode/NicMc/AdventOfCode2015/2/input.txt","r")
inputs = file.read().splitlines()
print(inputs[0])

class Present:
    def __init__(self,string):
        array = string.split('x')
        self.x = int(array[0])
        self.y = int(array[1])
        self.z = int(array[2])
    def getwrap(self):
        xy = self.x * self.y
        xz = self.x * self.z
        yz = self.y * self.z
        wrap = 2 * (xy + xz + yz) + min(xy,xz,yz)
        return wrap
    def getribbon(self):
        sort = sorted([self.x,self.y,self.z])
        small = 2 * (sort[0] + sort[1])
        cube = self.x * self.y * self.z
        return small + cube

total = 0
for inpu in inputs:
    total = total + Present(inpu).getwrap()

print("The fist answer is: {}".format(total))

total = 0
for inpu in inputs:
    total = total + Present(inpu).getribbon()

print("The second answer is: {}".format(total))

