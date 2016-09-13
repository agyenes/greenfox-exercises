
class HeroMove(object):

    def __init__(self):
        self.event = event
        self.keypressed = keypressed

    def move_down(event):
        char.move_down()
        screen_drawer(no_of_fields_h, no_of_fields_v)

    def move_up(event):
        char.move_up()
        screen_drawer(no_of_fields_h, no_of_fields_v)

    def move_left(event):
        char.move_left()
        screen_drawer(no_of_fields_h, no_of_fields_v)

    def move_right(event):
        char.move_right()
        screen_drawer(no_of_fields_h, no_of_fields_v)
