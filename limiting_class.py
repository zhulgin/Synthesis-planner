# Import external packages
import tkinter as tk
import ttkbootstrap as ttk
# Import constants from config file
from config import *
# Import chemicals dictionary
from chemicals import CHEMICALS


class Limiting(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master = parent)

        # Create labels
        self.create_kind_label()
        self.create_MW_label()
        self.create_eq_entry()
        
        # Create entries and dropdown
        self.create_dropdown()
        self.create_mmol_entry()
        self.create_mass_entry()
        self.create_volume_entry()
        
    # Creates a label stating if the chemical is the limiting reactant or not
    def create_kind_label(self):
        
        self.kind_var = tk.StringVar()
        
        ttk.Entry(self, 
            textvariable = self.kind_var, 
            state = 'disabled', 
            foreground = 'white', 
            width = COL_WIDTH).grid(
                column = 0, row = 0, 
                padx = PADX, pady = PADY)
        self.kind_var.set('Limiting reagent')

    # Creates label displaying molecular weight of selected chemical
    def create_MW_label(self):
        self.selection_MW_label = ttk.Label(self, 
            text = 'No chemical selected', 
            width = COL_WIDTH)
        self.selection_MW_label.grid(
            column = 1, row = 1, 
            padx = PADX, pady = PADY)

    # Label displaying eq of selected chemical
    def create_eq_entry(self):
        self.eq_var = tk.StringVar()
        self.eq_var.set(1)
        self.eq_entry = ttk.Entry(self, 
            textvariable = self.eq_var, 
            state = 'disabled', 
            style = 'info.TEntry', 
            foreground = 'white', 
            width = COL_WIDTH)
        self.eq_entry.grid(
            column = 5, row = 0, 
            padx = PADX, pady = PADY)
        ttk.Label(self, 
            text = 'eq.', 
            width = COL_WIDTH).grid(
                column = 5, row = 1, 
                padx = PADX, pady = PADY)

    # Entry for amount of substance. (Always disabled, just output)
    def create_mmol_entry(self):
        self.mmol_var = tk.StringVar()
        self.mmol_entry = ttk.Entry(self, 
            textvariable = self.mmol_var, 
            state = 'disabled', 
            style = 'info.TEntry', 
            foreground = 'white', 
            width = COL_WIDTH)
        self.mmol_entry.grid(
            column = 4, row = 0, 
            padx = PADX, pady = PADY)
        ttk.Label(self, 
            text = "Amount of\nsubstance (mmol)", 
            width = COL_WIDTH).grid(
                column = 4, row = 1, 
                padx = PADX, pady = PADY)



    # Creates dropdown menu for selecting chemical
    def create_dropdown(self):
        self.selection_var = tk.StringVar()
        self.selection_dropdown = ttk.Combobox(self, 
            textvariable = self.selection_var, 
            state = 'readonly', 
            width = COL_WIDTH - 2)
        self.selection_dropdown['values'] = list(CHEMICALS.keys())
        self.selection_dropdown.grid(
            column = 1, row = 0, 
            padx = PADX, pady = PADY)
        self.selection_dropdown.bind('<<ComboboxSelected>>', lambda event: self.update())
        
    # Entry for mass
    def create_mass_entry(self):
        self.mass_var = tk.StringVar()
        self.mass_entry = ttk.Entry(self, 
            textvariable = self.mass_var, 
            width = COL_WIDTH)
        self.mass_entry.grid(
            column = 2, row = 0, 
            padx = PADX, pady = PADY)
        ttk.Label(self, 
            text = 'Mass (mg)', 
            width = COL_WIDTH).grid(
                column = 2, row = 1, 
                padx = PADX, pady = PADY)

    # Entry for volume
    def create_volume_entry(self):
        self.volume_var = tk.StringVar()
        self.volume_entry = ttk.Entry(self, 
            textvariable = self.volume_var, 
            width = COL_WIDTH)
        self.volume_entry.grid(
            column = 3, row = 0, 
            padx = PADX, pady = PADY)
        ttk.Label(self, 
            text = 'Volume (mL)').grid(
                column = 3, row = 1, 
                padx = PADX, pady = PADY)


    

    # Updates molecular weight label, called when a chemical is selected from the dropdown menu
    def update(self):
        updated_MW = CHEMICALS[self.selection_var.get()]['MW']
        self.selection_MW_label.config(text = f'{updated_MW} g/mol')

        updated_state = CHEMICALS[self.selection_var.get()]['state']
        if updated_state == 'l':
            self.mass_entry.config(state = 'disabled', style = 'info.TEntry', foreground = 'white')
            self.volume_entry.config(state = 'enabled', style = 'success.TEntry')
        if updated_state == 's':
            self.volume_entry.config(state = 'disabled', style = 'info.TEntry', foreground = 'white')
            self.mass_entry.config(state = 'enabled', style = 'success.TEntry')

    # Calculate amount of substance and display in the entry box
    def calculate_n(self):

        if CHEMICALS[self.selection_var.get()]['state'] == 'l':

            chemical = CHEMICALS[self.selection_var.get()]
            v = float(self.volume_var.get())
            density = float(chemical['density'])

            m = (density * 10**3) * v # Multiply by 10^3 to get density in mg/mL instead of g/mL
            mw = chemical['MW']
            n = m / mw

            self.mass_var.set(m)
            self.mmol_var.set(round(n, 2))

        elif CHEMICALS[self.selection_var.get()]['state'] == 's':
        
            chemical = CHEMICALS[self.selection_var.get()]

            m = float(self.mass_entry.get())
            mw = float(chemical['MW'])
            n = m / mw

            self.mmol_var.set(round(n, 2))






    

    

    

    
        
        


