from tkinter import *
import math

root = Tk()

a = 600

canvas = Canvas(root, width = a, height = a, bg = 'yellow')
canvas.pack()

def draw_triangle(x, y, s):
    canvas.create_polygon([x, y, x + s, y, x + s/2, y + math.sqrt(3)/2 * s], fill='green', outline='black')

def fractal_drawer(x, y, s):
    draw_triangle(x, y, s)
    if s > 5:
        fractal_drawer(x, y, s/2)
        fractal_drawer(x + s/2, y, s/2)
        fractal_drawer(x + s/4, y + math.sqrt(3)/2 * s/2, s/2)

fractal_drawer(10, 10, 580)

root.mainloop()
