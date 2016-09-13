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
    for i in range(20):
        canvas.create_rectangle(10 + i*size, 10 + i*size, 10 + (i+1)*size, 10 + (i+1)*size, fill = color)

draw_square(10, '#b145f3')

root.mainloop()
