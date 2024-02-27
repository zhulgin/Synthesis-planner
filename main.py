# Import external packages
import tkinter as tk
import ttkbootstrap as ttk
# Import constants from config file
from config import *
# Import chemicals dictionary
from chemicals import CHEMICALS
# Import classes
from limiting_class import Limiting
from reactant_class import Reactant

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
        style = ttk.Style(theme = 'darkly')

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
        self.button_frame.grid(column = 0, row = self.rows, padx = PADX, pady = PADY)

        # Calculate button
        self.calculate_button = ttk.Button(self.button_frame, text = 'Calculate', command = lambda: self.calculate())
        self.calculate_button.pack(side = 'left', padx = PADX, pady = PADY)

        # Add button
        self.add_button = ttk.Button(self.button_frame, text = 'Add reactant', command = lambda: self.add_reactant())
        self.add_button.pack(side = 'left', padx = PADX, pady = PADY)

        self.rows += 1


    def create_limiting(self):
        self.limiting = Limiting(self)
        self.limiting.grid(column = 0, row = 1, padx = PADX, pady = PADY, sticky = 'w')

        self.rows += 1
        

    def add_reactant(self):
        new_reactant = Reactant(self)
        new_reactant.grid(column = 0, row = self.rows, padx = PADX, pady = PADY, sticky = 'w')
        self.reactants.append(new_reactant)

        self.rows += 1

    def calculate(self):
        self.limiting.calculate_n()
        limiting_n = float(self.limiting.mmol_var.get())

        try:
            for reactant in self.reactants:
                chemical_name = reactant.selection_var.get()
                chemical_state = CHEMICALS[chemical_name]['state']
                mw = CHEMICALS[chemical_name]['MW']
                eq = float(reactant.eq_var.get())
                n = eq * limiting_n
                m = n * mw

                reactant.mmol_var.set(round(n, 2))
                reactant.mass_var.set(round(m, 2))

                if chemical_state == 'l':

                    density = CHEMICALS[chemical_name]['density']
                    v = m / (density * 10**3) # Multiply by 10^3 to get density in mg/mL instead of g/mL
                    reactant.volume_var.set(round(v, 2))

                elif chemical_state == 's':
                    v = 'N/A'
                    reactant.volume_var.set(v)
        except:
            print('Invalid input')

    


if __name__ == "__main__":
    App()