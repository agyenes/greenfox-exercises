# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

side_1 = canvas.create_line(30, 30, 270, 30, fill='red')
side_2 = canvas.create_line(270, 30, 270, 270, fill='blue')
side_3 = canvas.create_line(270, 270, 30, 270, fill='green')
side_4 = canvas.create_line(30, 270, 30, 30, fill='cyan')

root.mainloop()
