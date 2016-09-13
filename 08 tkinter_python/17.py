from tkinter import *
import math

root = Tk()

canvas = Canvas(root, width='500', height='500', bg='white')
canvas.pack()

size = 20

for i in range(23):
    canvas.create_line(20 + i * size, 420, 250 + i * size/2, 20 + i * math.sqrt(3) * 10, fill='green')
    canvas.create_line(250 - i * size/2, 20 + i * math.sqrt(3) * 10, 480 - i * size, 420, fill='blue')
    canvas.create_line(480 - i * size/2, 420 - i * math.sqrt(3) * 10, 20 + i * size/2, 420 - i * math.sqrt(3) * 10, fill='red')

canvas.pack()

root.mainloop()
