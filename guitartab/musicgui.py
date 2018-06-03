
class SelectCursor:

    def __init__(self, x, y, width, height):
        # the size of one grid, since width and height are multiplied by 20
        self.width = 1
        self.height = 1

        self.start_x = 0
        self.start_y = 0
        # by pressing shift, the selector will be able to select more
        self.end_x = 0
        self.end_y = 0

        self.color = None

        self.current_staff = None

    def return_selected_notes(self):
        pass


class Staff:
    def __init__(self, notes):
        self.notes = notes


def update(canvas):
    canvas.clear()


def check_note_is_selected(note, selector):

    if note.x == selector.start_x and note.y == selector.start_y:
        return True
    elif selector.start_x <= note.x <= selector.end_y \
            and selector.start_y <= note.start_y <= selector.end_y:
        return True
    else:
        return False

