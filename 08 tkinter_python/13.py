# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

root = Tk()

a = 300
b = 300
size = 20

canvas = Canvas(root, width = a, height = b)
canvas.pack()

def draw_line(x, y):
    for i in range (0,16):
        canvas.create_line(i * size + x, 0, a/2, b/2)
        canvas.create_line(b, i * size + y, a/2, b/2)
        canvas.create_line(i * size + x, a, a/2, b/2)
        canvas.create_line(0, i * size + y, a/2, b/2)

draw_line(0, 0)

root.mainloop()
