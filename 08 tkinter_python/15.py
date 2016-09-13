# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

from tkinter import *

root = Tk()

a = 300

canvas = Canvas(root, width = a, height = a)
canvas.pack()

def lines(list):
    a = len(list)-1
    for i in range(a):
        canvas.create_line(list[i][0], list[i][1], list[i+1][0], list[i+1][1], fill='green')
    canvas.create_line(list[a][0], list[a][1], list[0][0], list[0][1], fill='green')

list1 = [[10, 10], [290,  10], [290, 290], [10, 290]]
list2 = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]

lines(list1)
lines(list2)

root.mainloop()
