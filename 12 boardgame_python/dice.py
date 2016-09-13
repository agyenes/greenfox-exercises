import random

class Dice(object):

    def roll_the_dice(self):
        return [random.randint(0,9), random.randint(0,9)]
