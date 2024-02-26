import tkinter as tk
import ttkbootstrap as ttk
from config import *
from chemicals import CHEMICALS
from chemical_row import Limiting_Reactant


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.setup()
        self.create_limiting()
        self.mainloop()

    def setup(self):
        ttk.Style(theme = 'darkly')
        self.title(APP_NAME)
        self.geometry(DIMENSIONS)
        self.resizable(False, False)
        self.bind('<Escape>', lambda event: self.destroy())

    def create_limiting(self):
        Limiting_Reactant(self, limiting = True).grid(column = 0, row = 0, padx = PAD_X, pady = PAD_Y)

    def calculate_mass(self):

        try:
            # Get inputs
            eq_ratio = float()
            limiting_mass = float()
            limiting_name = str()
            limiting_MW = float()

            chemical_name = str()
            chemical_MW = float()
            
            # Calculate mass
            mass_needed = eq_ratio * chemical_MW * limiting_mass / limiting_MW
        
            # Update result label
            # result_label.config(text=f"Mass needed: {mass_needed:.2f} g")

        except ValueError:
            # result_label.config(text="Invalid input")
            pass


    


if __name__ == "__main__":
    App()