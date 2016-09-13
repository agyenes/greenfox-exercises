from tkinter import *

root = Tk()

a = 600
b = 3

canvas = Canvas(root, width = a, height = a, bg = 'yellow')
canvas.pack()

def draw_rectangle(x, y, size):
    canvas.create_rectangle(x, y, x + size, y + size)

def fractal_drawer(x, y, size):
    draw_rectangle(x, y, size)
    if size > 5:
        fractal_drawer(x + size/3, y, size/3)
        fractal_drawer(x + size/3, y + 2 * size/3, size/3)
        fractal_drawer(x, y + size/3, size/3)
        fractal_drawer(x + 2 * size/3, y + size/3, size/3)

fractal_drawer(5, 5, 590)

root.mainloop()
