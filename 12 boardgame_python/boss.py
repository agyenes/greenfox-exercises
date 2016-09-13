from tkinter import *

class Boss(object):

    def __init__(self, boss_x, boss_y):
        self.boss_x = boss_x
        self.boss_y = boss_y
        self.boss_image = PhotoImage(file="assets/boss.png")

    def draw(self, canvas):
        canvas.create_image(self.boss_x * 72, self.boss_y * 72, anchor=NW, image=self.boss_image)
