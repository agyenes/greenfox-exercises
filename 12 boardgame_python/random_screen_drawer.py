def game_screen_drawer(h, v):
    for i in range (h):
        for j in range(v):
            image_type = random.randint(1, 2)
            if image_type == 1:
                canvas.create_image(i * field_size, j * field_size, anchor=NW, image=a)
            else:
                canvas.create_image(i * field_size, j * field_size, anchor=NW, image=b)
    canvas.create_image(hor_pos_hero, ver_pos_hero, anchor=NW, image=c)
