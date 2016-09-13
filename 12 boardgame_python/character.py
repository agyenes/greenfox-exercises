from tkinter import *

class Hero(object):

    def __init__(self, hero_x, hero_y, canvas):
        self.hero_x = hero_x
        self.hero_y = hero_y
        self.canvas = canvas
        self.hero_image = PhotoImage(file="assets/hero-down.png")

    def draw(self):
        self.canvas.create_image(self.hero_x * 72, self.hero_y * 72, anchor=NW, image=self.hero_image)

    def move_up(self):
        self.hero_y = self.hero_y - 1
        self.hero_image = PhotoImage(file="assets/hero-up.png")

    def move_down(self):
        self.hero_y = self.hero_y + 1
        self.hero_image = PhotoImage(file="assets/hero-down.png")

    def move_right(self):
        self.hero_x = self.hero_x + 1
        self.hero_image = PhotoImage(file="assets/hero-right.png")

    def move_left(self):
        self.hero_x = self.hero_x - 1
        self.hero_image = PhotoImage(file="assets/hero-left.png")

class Skeleton(object):

    def __init__(self, skeleton_x, skeleton_y, canvas):
        self.skeleton_x = skeleton_x
        self.skeleton_y = skeleton_y
        self.canvas = canvas
        self.skeleton_image = PhotoImage(file="assets/skeleton.png")

    def draw(self):
        self.canvas.create_image(self.skeleton_x * 72, self.skeleton_y * 72, anchor=NW, image=self.skeleton_image)

class Boss(object):

    def __init__(self, boss_x, boss_y, canvas):
        self.boss_x = boss_x
        self.boss_y = boss_y
        self.canvas = canvas
        self.boss_image = PhotoImage(file="assets/boss.png")

    def draw(self):
        self.canvas.create_image(self.boss_x * 72, self.boss_y * 72, anchor=NW, image=self.boss_image)
