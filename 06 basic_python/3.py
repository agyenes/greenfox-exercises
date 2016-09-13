# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Pirate():
  def __init__(self):
    self.number_of_calls = 0

  def drink_rum(self):
    self.number_of_calls += 1
    return self.number_of_calls

  def hows_goin_mate(self):
    if self.number_of_calls > 4:
      print("Arrrr!")
    else:
      print("Nothin")

pirate1 = Pirate()
pirate2 = Pirate()

pirate1.drink_rum()
pirate1.hows_goin_mate()
pirate1.drink_rum()
pirate1.hows_goin_mate()
pirate1.drink_rum()
pirate1.hows_goin_mate()
pirate1.drink_rum()
pirate1.hows_goin_mate()
pirate1.drink_rum()
pirate1.hows_goin_mate()
pirate1.drink_rum()
pirate1.hows_goin_mate()
pirate1.drink_rum()
pirate1.hows_goin_mate()
pirate1.drink_rum()
