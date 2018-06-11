
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

    def __init__(self, notes, x, y, top_margin=50, left_margin=40, width=800, line_thickness=1):
        self.notes = notes
        self.x = x
        self.y = y

        self.width = width
        self.line_thickness = line_thickness

        self.space_between_lines = 20
        self.top_margin = top_margin
        self.left_margin = left_margin

    def draw_staff(self, turtle):

        starting_x = self.x + self.left_margin
        starting_y = self.y - self.top_margin

        for i in range(0, 5):

            draw_rect(starting_x, starting_y,
                      self.width, self.line_thickness, "#000000", turtle)

            starting_y -= self.space_between_lines

        # bug where the last line of staff is blurry
        # draw another line over the last one
        draw_rect(starting_x, starting_y + self.space_between_lines,
                  self.width, self.line_thickness, "#000000", turtle)


def update(canvas):
    canvas.clear()


def draw_rect(x, y, width, height, color, turtle, multiplier=1):
    turtle.setheading(0)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.fillcolor(color)
    turtle.begin_fill()

    turtle.forward(width*multiplier)
    turtle.right(90)
    turtle.forward(height*multiplier)
    turtle.right(90)
    turtle.forward(width*multiplier)
    turtle.right(90)
    turtle.forward(height*multiplier)
    turtle.right(90)

    turtle.end_fill()


def check_note_is_selected(note, selector):

    if note.x == selector.start_x and note.y == selector.start_y:
        return True
    elif selector.start_x <= note.x <= selector.end_y \
            and selector.start_y <= note.start_y <= selector.end_y:
        return True
    else:
        return False

