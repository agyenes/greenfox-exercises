from tkinter import *
import math

root = Tk()

a = 800

canvas = Canvas(root, width = a, height = a, bg = 'cyan')
canvas.pack()

e = math.sqrt(3)/2

def draw_hexagon(x, y, s):
    canvas.create_polygon([x, y, x + s, y, x + (3/2) * s, y + e * s, x + s, y + 2 * e * s, x, y + 2 * e * s, x - 1/2 * s, y + e * s], fill='green', outline='yellow')

def fractal_drawer(x, y, s):
    draw_hexagon(x, y, s)
    if s > 4:
        fractal_drawer(x, y, s/2)
        fractal_drawer(x + 3/4 * s, y + e/2 * s, s/2)
        fractal_drawer(x, y + e * s, s/2)

#draw_hexagon(200, 50, 400)
fractal_drawer(200, 50, 400)

root.mainloop()
