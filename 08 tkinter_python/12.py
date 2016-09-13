# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=240, height=240, bg='white')
canvas.pack()

size = 30

for i in range(0,7,2):
    for j in range(0,7,2):
        canvas.create_rectangle(i * size, j * size, (i + 1) * size, (j + 1) * size, fill ='black')

for i in range(1,8,2):
    for j in range(1,8,2):
        canvas.create_rectangle(i * size, j * size, (i + 1) * size, (j + 1) * size, fill ='black')

root.mainloop()
