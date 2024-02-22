import tkinter as tk
import ttkbootstrap as ttk

from config import *
from config import *


class Reagent(ttk.Frame):

    def __init__(self, parent):
        super().__init__(master = parent)
        self.labels()

    def labels(self):
        self.testlabel = ttk.Label(master = self, text = "Test", width = 15)
        self.testlabel.grid(column = 0, row = 0)




class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.setup()
        self.widgets()
        self.mainloop()

    def setup(self):
        self.title(app_name)
        self.geometry(dimensions)
        self.resizable(False, False)
        self.bind('<Escape>', lambda event: self.destroy())

    def widgets(self):
        self.reagent = Reagent(self)
        self.reagent.grid(column = 0, row = 0)


    


if __name__ == "__main__":
    App()