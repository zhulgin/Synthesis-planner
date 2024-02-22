import tkinter as tk
import ttkbootstrap as ttk

from config import *
from config import *


class Chemical(ttk.Frame):

    def __init__(self, parent):
        super().__init__(master = parent)

        self.widgets()
        self.display_widgets



    def widgets(self):

        testlist = ["Select chemical", "hell", "o", "world"]

        self.selected_chemical = tk.StringVar()
        self.selected_chemical.set(testlist[0])

        self.chemical_dropdown = ttk.OptionMenu(self, self.selected_chemical, *testlist)
        self.chemical_dropdown.pack()

    def display_widgets(self):
        self.chemical_dropdown.grid(column = 1, row = 1)




class App(tk.Tk):
    def __init__(self):
        super().__init__()


        style = ttk.Style(theme = 'darkly')
        self.setup()
        self.widgets()
        self.mainloop()

    def setup(self):
        self.title(app_name)
        self.geometry(dimensions)
        self.resizable(False, False)
        self.bind('<Escape>', lambda event: self.destroy())

    def widgets(self):
        self.reagent = Chemical(self)
        self.reagent.grid(column = 0, row = 0)


    


if __name__ == "__main__":
    App()