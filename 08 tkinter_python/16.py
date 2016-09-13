# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300', bg='black')
canvas.pack()

i = 0

while i < 30:
    r = random.randint(1, 290)
    s = random.randint(1, 290)
    canvas.create_rectangle(r, s, r + 5, s + 5, fill='gray')
    i += 1

canvas.pack()

root.mainloop()
