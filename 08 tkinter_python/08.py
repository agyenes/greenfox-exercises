# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_square(a, b):
    canvas.create_rectangle(a, b, a + 50, b + 50, fill="green")

draw_square(30, 20)
draw_square(130, 110)
draw_square(220, 230)

root.mainloop()
