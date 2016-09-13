# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

a = 300
b = 300

canvas = Canvas(root, width=a, height=b)
canvas.pack()

def draw_square(c):
    canvas.create_rectangle(a/2 - c/2, b/2 - c/2, a/2 + c/2, b/2 + c/2, fill="green")

draw_square(56)
draw_square(170)
draw_square(230)

root.mainloop()
