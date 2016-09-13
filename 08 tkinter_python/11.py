# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *

root = Tk()

a = 300
b = 300

canvas = Canvas(root, width=a, height=b)
canvas.pack()

def draw_square(size, color):
    for i in range(7):
        canvas.create_rectangle(a/2 - (a/2)/(i+1), b/2 - (a/2)/(i+1), a/2 + (a/2)/(i+1), b/2 + (b/2)/(i+1), fill = color[i])

rainbow_colors = ['#ff0000', '#ff7f00', '#ffff00', '#000000', '#0000ff', '#4b0082', '#8f00ff']

draw_square(100, rainbow_colors)

root.mainloop()
