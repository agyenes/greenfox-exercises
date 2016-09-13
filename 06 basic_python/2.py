# Create a class called "Car"
# It should have a "type" property that stores the car's type in a string eg: "Mazda"
# It should have a "km" property that stores how many kilometers it have run
# The km and the type property should be a parmeter in the constructor
# It should have a method called "run" that takes a number and increments the "km" property by it

import math

class Car():
  def __init__(self, type, km):
    self.type = type
    self.km = km

  def ride(self, ride_km):
    return self.km + ride_km

my_mazda = Car("mazda", 12000)
print(my_mazda.type) # "mazda"
print(my_mazda.ride(100))
