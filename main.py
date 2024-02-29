# Import external packages
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
# Import constants from config file
from config import *
# Import chemicals dictionary
from chemicals import CHEMICALS
# Import classes and functions
from limiting_class import Limiting
from reactant_class import Reactant
from typst_pdf import typst_pdf

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.setup()
        self.create_frames()
        self.place_frames()
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
        # Variable to keep track of rows in calculations_frame
        self.rows = 0
        # List containing all added reactants
        self.reactants = []

    # Create frames to place widgets in
    def create_frames(self):
        # Create frame for help label
        self.help_frame = ttk.Frame(self)
        # Create fram for buttons
        self.button_frame = ttk.Frame(self)
        # Create frame for calculations (inputs and outputs)
        self.calculations_frame = ScrolledFrame(self, autohide = True)

    # Place the frames in the window using pack()
    def place_frames(self):
        self.help_frame.pack(anchor = 'w', padx = PADX, pady = PADY)
        self.button_frame.pack(padx = PADX, pady = PADY)
        self.calculations_frame.pack(fill = 'both', expand = 'yes', padx = PADX, pady = PADY)

    # Create widgets
    def create_widgets(self):
        self.create_help_label()
        self.create_buttons()
        self.create_limiting()
        
    # Place widgets into their respective frames
    def place_widgets(self):
        # Help frame
        self.help_label.pack(anchor = 'w')
        # Buttons frame
        self.calculate_button.pack(
            side = 'left', 
            padx = PADX, pady = PADY)
        self.add_button.pack(
            side = 'left', 
            padx = PADX, pady = PADY)
        self.export_button.pack(
            side = 'left', 
            padx = PADX, pady = PADY)
        self.rows += 1
        # Limiting frame
        self.limiting.grid(
            column = 0, row = self.rows, 
            padx = PADX, pady = PADY, 
            sticky = 'w')
        self.rows += 1

    # Create label explaining the colors
    def create_help_label(self):
        self.help_label = ttk.Label(self.help_frame, 
            text = HELP_LABEL,
            font = ('Arial', 9), foreground = 'gray')

    # Create the buttons
    def create_buttons(self):
        # Calculate button
        self.calculate_button = ttk.Button(self.button_frame,
            width = BUTTON_WIDTH,
            text = 'Calculate', 
            command = lambda: self.calculate())
        
        # Add button
        self.add_button = ttk.Button(self.button_frame, 
            width = BUTTON_WIDTH,
            text = 'Add reactant', 
            command = lambda: self.add_reactant())
        
        # Export button
        self.export_button = ttk.Button(self.button_frame, 
            width = BUTTON_WIDTH,
            text = 'Export pdf', 
            command = lambda: self.create_pdf())
    
    # Create the row where limiting reactant is specified
    def create_limiting(self):
        self.limiting = Limiting(self.calculations_frame)

    # Add a row for a non-limiting reactant. This function is called when the corresponding button is pressed.
    def add_reactant(self):
        new_reactant = Reactant(self.calculations_frame)
        new_reactant.grid(
            column = 0, row = self.rows, 
            padx = PADX, pady = PADY, 
            sticky = 'w')
        self.reactants.append(new_reactant)

        self.rows += 1

    # Do the calculations and update information in respective fields
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
                    v = ''
                    reactant.volume_var.set(v) 
        except:
            print('Invalid input')

    # Export experiment plan to pdf file using typst
    def create_pdf(self):
        try:
            self.calculate()
            limiting_name = self.limiting.selection_var.get()
            limiting_n = self.limiting.mmol_var.get()
            limiting_m = self.limiting.mass_var.get()
            limiting_v = self.limiting.volume_var.get()

            experiment_info = {
                limiting_name: {
                    'kind': 'Limiting',
                    'mass': limiting_m,
                    'volume': limiting_v,
                    'amount': limiting_n,
                    'eq': 1}}

            for reactant in self.reactants:
                name = reactant.selection_var.get()
                kind = reactant.kind_var.get()
                m = reactant.mass_var.get()
                v = reactant.volume_var.get()
                n = reactant.mmol_var.get()
                eq = reactant.eq_var.get()

                experiment_info[name] = {
                    'kind': kind,
                    'mass': m,
                    'volume': v,
                    'amount': n,
                    'eq': eq}
            typst_pdf(experiment_info)
        except:
            print('Export error')

# Run the application
if __name__ == "__main__":
    App()