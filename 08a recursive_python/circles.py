from tkinter import *

root = Tk()

a = 600

canvas = Canvas(root, width = a, height = a, bg = 'yellow')
canvas.pack()

def fractal_drawer(x, y, size):
    canvas.create_oval(x, y, x + size, y + size, fill="yellow")
    if size < 5:
        pass
    else:
        fractal_drawer(x, y, size/2)
        fractal_drawer(x+size/2, y+size/2, size/2)

print(fractal_drawer(5, 5, 590))

root.mainloop()
