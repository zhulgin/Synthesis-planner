import tkinter as tk
import ttkbootstrap as ttk
from config import *
from chemicals import CHEMICALS


class Limiting_Reactant(ttk.Frame):
    def __init__(self, parent, limiting = False):
        super().__init__(master = parent)

        self.limiting = limiting

        # Create labels
        self.create_kind_label()
        self.create_MW_label()
        self.create_eq_label()
        self.create_state_label()

        # Create entries and dropdown
        self.create_dropdown()
        self.create_mass_entry()
        self.create_volume_entry()
        
    # Creates a label stating if the chemical is the limiting reactant or not
    def create_kind_label(self):
        if self.limiting == False:
            kind_label = 'Reagent'
        elif self.limiting == True:
            kind_label = 'Limiting reactant'

        ttk.Label(self, text = kind_label, width = 16).grid(column = 0, row = 0, padx = PAD_X, pady = PAD_Y)

    # Creates label displaying molecular weight of selected chemical
    def create_MW_label(self):
        self.selection_MW_label = ttk.Label(self, text = 'No chemical selected')
        self.selection_MW_label.grid(column = 1, row = 1, padx = PAD_X, pady = PAD_Y)

    # Label displaying eq of selected chemical
    def create_eq_label(self):
        ttk.Label(self, text = '1 eq.').grid(column = 6, row = 0, padx = PAD_X, pady = PAD_Y)

    # Label displaying state of selected chemical
    def create_state_label(self):
        self.selection_state_label = ttk.Label(self, text = '')
        self.selection_state_label.grid(column = 1, row = 2, padx = PAD_X, pady = PAD_Y)



    # Creates dropdown menu for selecting chemical
    def create_dropdown(self):
        self.selection_var = tk.StringVar()
        self.selection_dropdown = ttk.Combobox(self, textvariable = self.selection_var, state = 'readonly')
        self.selection_dropdown['values'] = list(CHEMICALS.keys())
        self.selection_dropdown.grid(column = 1, row = 0, padx = PAD_X, pady = PAD_Y)
        self.selection_dropdown.bind('<<ComboboxSelected>>', lambda event: self.update())
        
    # Entry for mass
    def create_mass_entry(self):
        self.mass_var = tk.StringVar()
        self.mass_entry = ttk.Entry(self, textvariable = self.mass_var)
        self.mass_entry.grid(column = 2, row = 0, padx = PAD_X, pady = PAD_Y)
        ttk.Label(self, text = 'mg').grid(column = 2, row = 1, padx = PAD_X, pady = PAD_Y)

    # Entry for volume
    def create_volume_entry(self):
        self.volume_var = tk.StringVar()
        self.volume_entry = ttk.Entry(self, textvariable = self.volume_var)
        self.volume_entry.grid(column = 4, row = 0, padx = PAD_X, pady = PAD_Y)
        ttk.Label(self, text = 'mL').grid(column = 4, row = 1, padx = PAD_X, pady = PAD_Y)


    

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

    

    

    

    
        
        


