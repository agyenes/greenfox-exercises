from tkinter import *
import random

class Stats(object):

    def __init__(self, x, y):
        self.boss_x = boss_x
        self.boss_y = boss_y

    def draw(self, canvas):
        print('Hero (Level 1) HP: 8/10 | DP: 8 | SP: 6')

from tkinter import *

root = Tk()

a = 300
b = 300

canvas = Canvas(root, width=a, height=b)
canvas.pack()

root.mainloop()
