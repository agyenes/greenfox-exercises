from tkinter import *

class Skeleton(object):

    def __init__(self, skeleton_x, skeleton_y):
        self.skeleton_x = skeleton_x
        self.skeleton_y = skeleton_y
        self.skeleton_image = PhotoImage(file="assets/skeleton.png")

    def draw(self, canvas):
        canvas.create_image(self.skeleton_x * 72, self.skeleton_y * 72, anchor=NW, image=self.skeleton_image)
