# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

root = Tk()

a = 300
b = 300

canvas = Canvas(root, width=a, height=b)
canvas.pack()

canvas.create_rectangle(a/2 - 150, b/2 - 150, a/2 - 130, b/2 - 130, fill="green")
canvas.create_rectangle(a/2 - 120, b/2 - 130, a/2, b/2, fill="cyan")
canvas.create_rectangle(a/2, b/2, a/2 + 30, b/2 + 40, fill="blue")
canvas.create_rectangle(a/2 + 100, b/2 + 100, a, b, fill="red")

root.mainloop()
