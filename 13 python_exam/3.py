# Create a class that represents a cuboid:
# It should take it's three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume
#
class Cuboid:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getSurface(self):
        surface = 2 * (self.a * self.b + self.b * self.c + self.a * self.c)
        return surface

    def getVolume(self):
        volume = self.a * self.b * self.c
        return volume

cuboid1 = Cuboid(7, 8, 9)
cuboid2 = Cuboid(3, 4, 2)

print(cuboid1.getSurface())
print(cuboid2.getSurface())
print(cuboid1.getVolume())
print(cuboid2.getVolume())
