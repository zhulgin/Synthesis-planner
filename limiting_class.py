import tkinter as tk
import ttkbootstrap as ttk
from config import *
from chemicals import CHEMICALS


class Limiting(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master = parent)

        # Create labels
        self.create_kind_label()
        self.create_MW_label()
        self.create_eq_label()
        self.create_state_label()
        
        # Create entries and dropdown
        self.create_dropdown()
        self.create_mmol_entry()
        self.create_mass_entry()
        self.create_volume_entry()
        
    # Creates a label stating if the chemical is the limiting reactant or not
    def create_kind_label(self):

        kind_label = 'Limiting reactant'
        ttk.Label(self, text = kind_label, width = KIND_COLUMN_WIDTH).grid(column = 0, row = 0, padx = PADX, pady = PADY)

    # Creates label displaying molecular weight of selected chemical
    def create_MW_label(self):
        self.selection_MW_label = ttk.Label(self, text = 'No chemical selected')
        self.selection_MW_label.grid(column = 1, row = 1, padx = PADX, pady = PADY)

    # Label displaying eq of selected chemical
    def create_eq_label(self):
        ttk.Label(self, text = '1 eq.').grid(column = 7, row = 0, padx = PADX, pady = PADY)

    # Label displaying state of selected chemical
    def create_state_label(self):
        self.selection_state_label = ttk.Label(self, text = '')
        self.selection_state_label.grid(column = 1, row = 2, padx = PADX, pady = PADY)

    # Entry for amount of substance. (Always disabled, just output)
    def create_mmol_entry(self):
        self.mmol_var = tk.StringVar()
        self.mmol_entry = ttk.Entry(self, textvariable = self.mmol_var, state = 'disabled')
        self.mmol_entry.grid(column = 6, row = 0, padx = PADX, pady = PADY)
        ttk.Label(self, text = "Amount of substance (mmol)").grid(column = 6, row = 1, padx = PADX, pady = PADY)



    # Creates dropdown menu for selecting chemical
    def create_dropdown(self):
        self.selection_var = tk.StringVar()
        self.selection_dropdown = ttk.Combobox(self, textvariable = self.selection_var, state = 'readonly')
        self.selection_dropdown['values'] = list(CHEMICALS.keys())
        self.selection_dropdown.grid(column = 1, row = 0, padx = PADX, pady = PADY)
        self.selection_dropdown.bind('<<ComboboxSelected>>', lambda event: self.update())
        
    # Entry for mass
    def create_mass_entry(self):
        self.mass_var = tk.StringVar()
        self.mass_entry = ttk.Entry(self, textvariable = self.mass_var)
        self.mass_entry.grid(column = 2, row = 0, padx = PADX, pady = PADY)
        ttk.Label(self, text = 'Mass (mg').grid(column = 2, row = 1, padx = PADX, pady = PADY)

    # Entry for volume
    def create_volume_entry(self):
        self.volume_var = tk.StringVar()
        self.volume_entry = ttk.Entry(self, textvariable = self.volume_var)
        self.volume_entry.grid(column = 4, row = 0, padx = PADX, pady = PADY)
        ttk.Label(self, text = 'Volume (mL)').grid(column = 4, row = 1, padx = PADX, pady = PADY)


    

    # Updates molecular weight label, called when a chemical is selected from the dropdown menu
    def update(self):
        updated_MW = CHEMICALS[self.selection_var.get()]['MW']
        self.selection_MW_label.config(text = f'{updated_MW} g/mol')

        updated_state = CHEMICALS[self.selection_var.get()]['state']
        if updated_state == 'l':
            self.mass_entry.config(state = 'disabled')
            self.volume_entry.config(state = 'enabled')
            self.selection_state_label.config(text = 'Liquid')
        if updated_state == 's':
            self.volume_entry.config(state = 'disabled')
            self.mass_entry.config(state = 'enabled')
            self.selection_state_label.config(text = 'Solid')

    # Calculate amount of substance and display in the entry box
    def calculate_n(self):

        try:

            if CHEMICALS[self.selection_var.get()]['state'] == 'l':

                chemical = CHEMICALS[self.selection_var.get()]
                v = float(self.volume_var.get())
                density = float(chemical['density'])

                m = density * v * (10**3)
                mw = chemical['MW']
                n = m / mw

                self.mass_var.set(m)
                self.mmol_var.set(round(n, 1))

            elif CHEMICALS[self.selection_var.get()]['state'] == 's':
            
                chemical = CHEMICALS[self.selection_var.get()]

                m = float(self.mass_entry.get())
                mw = float(chemical['MW'])
                n = m / mw

                self.mmol_var.set(round(n, 1))

        except ValueError:
            print('Invalid input')




    

    

    

    
        
        


