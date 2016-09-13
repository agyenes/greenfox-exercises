# reproduce this: [image link]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [image link]
# can you make the colors change? make every line a different color.

from tkinter import *

root = Tk()

a = 300
size = 10

canvas = Canvas(root, width = a, height = a)
canvas.pack()

for i in range (1,16):
    canvas.create_line(a/2, a/2 - i * size, i * size, a/2, fill='green')

for i in range (1,15):
    canvas.create_line(a/2 + i * size, a/2, a/2, i * size, fill='green')

for i in range (1,15):
    canvas.create_line(a/2, a/2 + i * size, a - i * size, a/2, fill='green')

for i in range (1,16):
    canvas.create_line(a/2, a/2 + i * size, i * size, a/2, fill='green')



root.mainloop()
