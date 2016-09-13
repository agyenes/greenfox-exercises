# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area

import math

class Circle():
  def __init__(self, radius):
    self.radius = radius

  def get_circumference(self):
      return self.radius * 2 * math.pi

  def get_area(self):
      return self.radius ** 2 * math.pi

circle1 = Circle(5)
print(circle1.get_circumference())
print(circle1.get_area())
