from tkinter import *
import turtle
import guitartab.musicgui
import tkinter.filedialog as tk
import tkinter.messagebox as tk2


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.turtle = None
        self.grid_canvas_multiplier = 20
        self.screen = None
        self.create_widgets()

    def create_widgets(self):
        # self.text1 = Text(width=20, height=20)
        # self.text1.pack(expand=YES, fill=BOTH)  # to make the textbox fill entire window

        self.grid_canvas_multiplier = 20

        self.screen = Canvas(master=self.master, width=500, height=500)
        self.screen.pack(expand=YES, fill=BOTH)

    def draw(self):
        pass


root = Tk()
root.title('Text Editor')
root.geometry('600x700')
root.wm_maxsize(600, 700)
root.wm_minsize(600, 700)
app = Application(root)
app.mainloop()
