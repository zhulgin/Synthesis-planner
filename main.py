# Import external packages
import tkinter as tk
import ttkbootstrap as ttk
# Import constants from config file
from config import *
# Import chemicals dictionary
from chemicals import CHEMICALS
# Import classes and functions
from limiting_class import Limiting
from reactant_class import Reactant
from export_pdf import export_pdf

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.setup()
        self.create_widgets()
        self.place_widgets()
        self.mainloop()

    # Set properties, style, variables etc.
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
        # Create frame for calculations (inputs and outputs)
        self.calculations_frame = ttk.Frame(self)
        # Variable to keep track of rows in calculations_frame
        self.rows = 0
        # List containing all added reactants
        self.reactants = []

    def create_widgets(self):
        self.create_buttons()
        self.create_limiting()
        self.create_help_label()

    def create_frames(self):
        pass

    def place_widgets(self):

        self.calculations_frame.pack()


    def create_buttons(self):
        # Frame for buttons
        self.button_frame = ttk.Frame(self.calculations_frame)
        self.button_frame.grid(
            column = 0, row = self.rows, 
            padx = PADX, pady = PADY)
        # Calculate button
        self.calculate_button = ttk.Button(self.button_frame,
            width = BUTTON_WIDTH,
            text = 'Calculate', 
            command = lambda: self.calculate())
        self.calculate_button.pack(
            side = 'left', 
            padx = PADX, pady = PADY)
        # Add button
        self.add_button = ttk.Button(self.button_frame, 
            width = BUTTON_WIDTH,
            text = 'Add reactant', 
            command = lambda: self.add_reactant())
        self.add_button.pack(
            side = 'left', 
            padx = PADX, pady = PADY)
        # Export button
        self.export_button = ttk.Button(self.button_frame, 
            width = BUTTON_WIDTH,
            text = 'Export pdf', 
            command = lambda: self.create_pdf())
        self.export_button.pack(
            side = 'left', 
            padx = PADX, pady = PADY)

        self.rows += 1


    def create_limiting(self):
        self.limiting = Limiting(self.calculations_frame)
        self.limiting.grid(
            column = 0, row = self.rows, 
            padx = PADX, pady = PADY, 
            sticky = 'w')

        self.rows += 1
        

    def create_help_label(self):
        self.help_label = ttk.Label(self, 
            text = 'Green = input\nBlue = output',
            font = ('Arial', 12))
        self.help_label.pack(anchor = 'w')

    def add_reactant(self):
        new_reactant = Reactant(self.calculations_frame)
        new_reactant.grid(
            column = 0, row = self.rows, 
            padx = PADX, pady = PADY, 
            sticky = 'w')
        self.reactants.append(new_reactant)

        self.rows += 1

    def calculate(self):
        try:
            self.limiting.calculate_n()

            limiting_n = float(self.limiting.mmol_var.get())

            for reactant in self.reactants:
                
                chemical_name = reactant.selection_var.get()
                mw = CHEMICALS[chemical_name]['MW']
                eq = float(reactant.eq_var.get())
                n = eq * limiting_n
                m = n * mw
                v = float()

                reactant.mmol_var.set(round(n, 2))
                reactant.mass_var.set(round(m, 2))

                if CHEMICALS[chemical_name]['state'] == 'l':
                    density = CHEMICALS[chemical_name]['density']
                    v = m / (density * 10**3) # Multiply by 10^3 to get density in mg/mL instead of g/mL
                    reactant.volume_var.set(round(v, 2))

                elif CHEMICALS[chemical_name]['state'] == 's':
                    v = 'N/A'
                    reactant.volume_var.set(v)

                
        
        except:
            print('Invalid input')

    def create_pdf(self):
        
        try:
            self.calculate()
            limiting_name = self.limiting.selection_var.get()
            limiting_n = self.limiting.mmol_var.get()
            limiting_m = self.limiting.mass_var.get()
            limiting_v = self.limiting.volume_var.get()

            experiment_info = {
                limiting_name: {
                    'mass': limiting_m,
                    'volume': limiting_v,
                    'amount': limiting_n,
                    'eq': 1
                }
            }

            for reactant in self.reactants:
                name = reactant.selection_var.get()
                m = reactant.mass_var.get(),
                v = reactant.volume_var.get()
                n = reactant.mmol_var.get()
                eq = reactant.eq_var.get()

                experiment_info[name] = {
                    'mass': m,
                    'volume': v,
                    'amount': n,
                    'eq': eq
                }
            export_pdf(experiment_info)
        except:
            print('Export error')
    

if __name__ == "__main__":
    App()