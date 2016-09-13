# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *

root = Tk()

a = 300
b = 300

canvas = Canvas(root, width=a, height=b)
canvas.pack()

def draw_square(c):
    for i in range(20):
        canvas.create_rectangle(a/2 - c/2, b/2 - c/2, a/2 + c/2, b/2 + c/2, fill="green")

draw_square(56)

root.mainloop()
