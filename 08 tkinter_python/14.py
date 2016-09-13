# reproduce this: [image link]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [image link]
# can you make the colors change? make every line a different color.

from tkinter import *

root = Tk()

a = 300
b = 300
size = 20

canvas = Canvas(root, width = a, height = b)
canvas.pack()

for i in range (0,15):
    canvas.create_line(0, i * size, i * size, 15 * size, fill='green')
    canvas.create_line(i * size, 0, 15 * size, i * size, fill='purple')

root.mainloop()
