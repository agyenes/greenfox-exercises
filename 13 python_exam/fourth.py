# Create a Rocket class
# It should take 3 parameters in its constructor
# 1st parameter: the type of the rocket as a string, "falcon1" or "falcon9"
# 2nd parameter: the starting fuel level as a number
# 3rd parameter: number of launches as a number

class Rocket(object):

    def __init__(self, type, fuel, launches = 0):
        self.type = type
        self.fuel = fuel
        self.launches = launches

# launch()
# it should use 1 fuel if it's a falcon1 and 9 if it's a falcon9
# it should increment the launches by one

    def launch(self):
        if self.type == 'falcon1':
            self.fuel -=1
            self.launches += 1
        elif self.type == 'falcon9':
            self.fuel -= 9
            self.launches += 1

# refill()
# it should refill the rocket's fuel level to 5 if falcon1 and to 20 if falcon9
# it should return the used fuel
# example: if the rocket is a falcon1 and has fuel level 3, then it should return 2

    def refill(self, type):
        if self.type == 'falcon1':
            used_fuel = 5 - self.fuel
            self.fuel = 5
            return used_fuel
        elif self.type == 'falcon9':
            used_fuel = 20 - self.fuel
            self.fuel = 20
            return used_fuel

# getStats()
# it should return its stats as a string like: "name: falcon9, fuel: 11"

    def getStats(self):
        return 'name: ' + self.type + ', fuel: ' + str(self.fuel)

# class falcon1(Rocket):
#     def __init__(self):
#         super().__init__()
#         self.type = 'falcon1'
#         self.fuel = 0
#         self.launches = 0
#
# class falcon9(Rocket):
#     def __init__(self):
#         super().__init__()
#         self.type = 'falcon1'
#         self.fuel = 0
#         self.launches = 0
#
# class returned_falcon9(Rocket):
#     def __init__(self):
#         super().__init__()
#         self.type = 'falcon1'
#         self.fuel = 11
#         self.launches = 1

# Create a SpaceX class
# it should take 1 parameter in its constructor
# 1st parameter: the stored fuel

class SpaceX(object):

    def __init__(self, stored_fuel):
        self.stored_fuel = stored_fuel
        self.rockets = []
        self.launches = 0
        self.used_fuel = 0

# addRocket(rocket)
# it should add a new rocket to SpaceX that is given in its first parameter

    def addRocket(self, type):
        self.type = type
        self.rockets.append(type)

# refill_all()
# it should refill all of its rockets with fuel and substract the needed fuel from the storage

    def refill_all(self):
        sum = 0
        for rocket in self.rockets:
            sum += rocket.refill(self.type)
        self.stored_fuel -= sum

# launch_all()
# it should launch all the rockets

    def launch_all(self):
        for rocket in self.rockets:
            rocket.launch()
            self.launches += 1

# buy_fuel(amount)
# it should increase stored fuel by amount

    def buy_fuel(self, amount):
        self.stored_fuel += amount

# getStats()
# it should return its stats as a sting like: "rockets: 3, fuel: 100, launches: 1"

    def getStats(self):
        rocket_counter = 0
        launch_counter = 0
        for rocket in self.rockets:
            rocket_counter += 1
            launch_counter += rocket.launches
        return 'rockets: ' + str(rocket_counter) + ', fuel: ' + str(self.stored_fuel) + ' launches: ' + str(launch_counter)

# The following code should work with the classes

space_x = SpaceX(100)
falcon1 = Rocket('falcon1', 0, 0)
falcon9 = Rocket('falcon9', 0, 0)
returned_falcon9 = Rocket('falcon9', 11, 1)

print(returned_falcon9.getStats()) # name: falcon9, fuel: 11

space_x.addRocket(falcon1)
space_x.addRocket(falcon9)
space_x.addRocket(returned_falcon9)

print(space_x.getStats()) # rockets: 3, fuel: 100, launches: 1
space_x.refill_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 1
space_x.launch_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 4
space_x.buy_fuel(50)
print(space_x.getStats()) # rockets: 3, fuel: 116, launches: 4
