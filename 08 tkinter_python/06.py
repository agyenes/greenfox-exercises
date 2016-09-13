# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import *

root = Tk()

a = 300
b = 300

canvas = Canvas(root, width=a, height=b)
canvas.pack()

canvas.create_rectangle(a/2 - 5, b/2 - 5, a/2 + 5, b/2 + 5, fill="green")

root.mainloop()
