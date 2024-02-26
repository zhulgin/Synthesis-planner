import tkinter as tk
import ttkbootstrap as ttk
from config import *
from chemicals import CHEMICALS
from limiting_reactant_class import Limiting_Reactant


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.rows = 0
        self.reactants = []

        self.setup()
        self.create_buttons()
        self.create_limiting()
        

        self.mainloop()

    def setup(self):

        # Presentation
        ttk.Style(theme = 'darkly')
        self.title(APP_NAME)
        self.geometry(DIMENSIONS)
        self.resizable(True, True)
        self.iconbitmap(APP_ICON)

        # Key bindings
        self.bind('<Escape>', lambda event: self.destroy())
        self.bind('<Return>', lambda event: self.calculate())

    def create_buttons(self):

        # Frame for buttons
        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(column = 0, row = self.rows, padx = PAD_X, pady = PAD_Y)

        # Calculate button
        self.calculate_button = ttk.Button(self.button_frame, text = 'Calculate', command = lambda: self.calculate())
        self.calculate_button.pack(side = 'left', padx = PAD_X, pady = PAD_Y)

        # Add button
        self.add_button = ttk.Button(self.button_frame, text = 'Add reactant', command = lambda: self.add_reactant())
        self.add_button.pack(side = 'left', padx = PAD_X, pady = PAD_Y)

        self.rows += 1


    def create_limiting(self):
        self.limiting_row = Limiting_Reactant(self, limiting = True)
        self.limiting_row.grid(column = 0, row = 1, padx = PAD_X, pady = PAD_Y)

        self.rows += 1
        

    def add_reactant(self):

        print('Adds reactant')

        new_reactant = Limiting_Reactant(self, limiting = False)
        new_reactant.grid(column = 0, row = self.rows, padx = PAD_X, pady = PAD_Y)

        self.rows += 1




    def calculate(self):
        print('Calculating!')

    


if __name__ == "__main__":
    App()