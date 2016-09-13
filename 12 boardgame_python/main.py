from tkinter import *
import random
from character import Hero
from character import Skeleton
from character import Boss
from move import HeroMove
from dice import Dice

root = Tk()

canvas = Canvas(root, width = 720, height = 800, bg='white')

class DrawMap(object):

    def __init__(self):
        self.no_of_fields_h = 10
        self.no_of_fields_v = 10
        self.field_size = 72
        self.floor_image = PhotoImage(file="assets/floor.png")
        self.wall_image = PhotoImage(file="assets/wall.png")
        self.canvas = canvas
        self.dice = Dice()

        dice_result_1 = self.dice.roll_the_dice()
        self.hero = Hero(dice_result_1[0], dice_result_1[1], canvas)
        self.draw_hero(dice_result_1)

        dice_result_2 = self.dice.roll_the_dice()
        self.boss = Boss(dice_result_2[0], dice_result_2[1], canvas)
        self.draw_boss(dice_result_2)

        dice_result_3 = self.dice.roll_the_dice()
        self.skeleton_1 = Skeleton(dice_result_3[0], dice_result_3[1], canvas)
        self.draw_skeleton_1(dice_result_3)

        dice_result_4 = self.dice.roll_the_dice()
        self.skeleton_2 = Skeleton(dice_result_4[0], dice_result_4[1], canvas)
        self.draw_skeleton_2(dice_result_4)

        dice_result_5 = self.dice.roll_the_dice()
        self.skeleton_3 = Skeleton(dice_result_5[0], dice_result_5[1], canvas)
        self.draw_skeleton_3(dice_result_5)

        self.map_1 = [[1,0,0,1,0,1,0,0,0,0],
                    [0,0,0,1,0,1,0,1,1,0],
                    [0,1,1,1,0,1,0,1,1,0],
                    [0,0,0,0,0,1,0,0,0,0],
                    [1,1,1,1,0,1,1,1,1,0],
                    [0,1,0,1,0,0,0,0,1,0],
                    [0,1,0,1,0,0,0,0,1,0],
                    [0,0,0,0,0,1,1,0,1,0],
                    [0,1,1,1,0,0,0,0,1,0],
                    [0,0,0,1,0,1,1,0,1,0],
                    [0,1,0,1,0,1,0,0,0,0]]

    def screen_drawer(self):
        for i in range(self.no_of_fields_h):
            for j in range(self.no_of_fields_v):
                if self.map_1[j][i] == 0:
                    self.canvas.create_image(i * self.field_size, j * self.field_size, anchor=NW, image=self.floor_image)
                elif self.map_1[j][i] == 1:
                    self.canvas.create_image(i * self.field_size, j * self.field_size, anchor=NW, image=self.wall_image)

    def draw_hero(dice_result_1):
        if self.map_1.is_obstacle(dice_result_1[0], dice_result_1[1]) == False:
            self.hero = Hero(dice_result_1[0], dice_result_1[1], canvas)
            self.hero.draw()
        else:
            draw_hero(dice_result_1)

    def draw_boss(dice_result_2):
        if self.map_1.is_obstacle(dice_result_2[0], dice_result_2[1]) == False:
            self.boss = Boss(dice_result_2[0], dice_result_2[1], canvas)
            self.boss.draw()
        else:
            draw_boss(dice_result_2)

    def draw_skeleton_1(dice_result_3):
        if self.map_1.is_obstacle(dice_result_3[0], dice_result_3[1]) == False:
            self.skeleton_1 = Skeleton(dice_result_3[0], dice_result_3[1], canvas)
            self.skeleton_1.draw()
        else:
            draw_skeleton_1(dice_result_3)

    def draw_skeleton_2(dice_result_4):
        if self.map_1.is_obstacle(dice_result_4[0], dice_result_4[1]) == False:
            self.skeleton_2 = Skeleton(dice_result_4[0], dice_result_4[1], canvas)
            self.skeleton_2.draw()
        else:
            draw_skeleton_2(dice_result_4)

    def draw_skeleton_3(dice_result_5):
        if self.map_1.is_obstacle(dice_result_5[0], dice_result_5[1]) == False:
            self.skeleton_3 = Skeleton(dice_result_5[0], dice_result_5[1], canvas)
            self.skeleton_3.draw()
        else:
            draw_skeleton_3(dice_result_5)

    def stats_drawer(self):
        self.info_box_height = 80
        self.canvas.create_rectangle(0, self.field_size * self.no_of_fields_v, self.field_size * self.no_of_fields_h, self.field_size * self.no_of_fields_h + self.info_box_height, fill="grey")
        self.canvas.create_rectangle(10, self.field_size * self.no_of_fields_v + 10, self.field_size * self.no_of_fields_h + 10, self.field_size * self.no_of_fields_h + self.info_box_height - 10, fill="white")
        self.canvas.create_text(self.field_size * self.no_of_fields_h/2, self.field_size * self.no_of_fields_h + self.info_box_height/2, text='Hero (Level 1) HP: 8/10 | DP: 8 | SP: 6', font=('Arial', 24, 'bold'))

    def is_obstacle(self, x, y):
        if self.map_1[x][y] == 0:
            return True
        else:
            return False

    def move_down(event):
        self.hero.move_down()
        screen_drawer(no_of_fields_h, no_of_fields_v)

    def move_up(event):
        self.hero.move_up()
        screen_drawer(no_of_fields_h, no_of_fields_v)

    def move_left(event):
        self.hero.move_left()
        screen_drawer(no_of_fields_h, no_of_fields_v)

    def move_right(event):
        self.hero.move_right()
        screen_drawer(no_of_fields_h, no_of_fields_v)

starting_map = DrawMap()
starting_map.screen_drawer()
starting_map.stats_drawer()

root.bind("<Up>", starting_map.move_up)
root.bind("<Down>", starting_map.move_down)
root.bind("<Right>", starting_map.move_right)
root.bind("<Left>", starting_map.move_left)

canvas.pack()

root.mainloop()
