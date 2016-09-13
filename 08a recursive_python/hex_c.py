from tkinter import *
import math

root = Tk()

a = 900

canvas = Canvas(root, width = a, height = a, bg = 'blue')
canvas.pack()

e = math.sqrt(3)/2

def draw_hexagon(x, y, s):
    canvas.create_polygon([x, y, x + s, y, x + (1 + 1/2) * s, y + e * s, x + s, y + 2 * e * s, x, y + 2 * e * s, x - 1/2 * s, y + e * s], fill='brown', outline='white')
    canvas.create_oval(x - e*s/3, y, x + s + e*s/3, y + 2 * e * s, outline='cyan')

def fractal_drawer(x, y, s):
    draw_hexagon(x, y, s)
    if s > 8:
        fractal_drawer(x, y, s/3)
        fractal_drawer(x + 2 * s/3, y, s/3)
        fractal_drawer(x - s/3, y + e * s *2/3, s/3)
        fractal_drawer(x + s, y + e * s *2/3, s/3)
        fractal_drawer(x, y + e * s *4/3, s/3)
        fractal_drawer(x + 2 * s/3, y + e * s * 4/3, s/3)

#draw_hexagon(200, 50, 400)
fractal_drawer(250, 50, 400)

root.mainloop()
