# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300, bg='white')
canvas.pack()

def draw_square(size, color):
    offset = 10
    for i in range(1, 7):
        a = (size * i)
        offset += size * (i - 1)
        canvas.create_rectangle(offset, offset, a + offset, a + offset, fill = color)

draw_square(10, '#b145f3')

root.mainloop()
