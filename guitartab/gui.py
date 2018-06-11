from tkinter import *
import turtle
import guitartab.musicgui as gui
import tkinter.filedialog as tk
import tkinter.messagebox as tk2


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid_canvas_multiplier = 20

        self.turtle = None
        self.screen = None
        self.canvas = None

        self.create_widgets()
        self.draw()

    def create_widgets(self):

        self.grid_canvas_multiplier = 20

        self.canvas = Canvas(master=self.master, width=width, height=height)
        self.canvas.pack(expand=YES, fill=BOTH)

        self.turtle = turtle.RawTurtle(self.canvas)
        self.screen = self.turtle.getscreen()

        self.turtle.hideturtle()
        self.turtle.speed(1)
        self.screen.tracer(0, 0)
        self.turtle.home()

        self.turtle.pencolor("#000000")

    def draw(self):
        x = -width / 2
        y = height / 2
        space_between_staffs = 140

        staffs = []

        for i in range(1,6):
            temp = gui.Staff(None, x, y)
            temp.draw_staff(self.turtle)

            staffs.append(temp)
            y -= space_between_staffs


width = 900
height = 750

root = Tk()
root.title('Text Editor')
root.geometry(str(width) + 'x' + str(height))
root.wm_maxsize(width, height)
root.wm_minsize(width, height)

app = Application(root)
app.mainloop()
