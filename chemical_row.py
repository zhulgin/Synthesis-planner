import tkinter as tk
import ttkbootstrap as ttk
from config import *
from chemicals import CHEMICALS


class Limiting_Reactant(ttk.Frame):
    def __init__(self, parent, limiting = False):
        super().__init__(master = parent)

        self.limiting = limiting
        self.set_kind_label()
        self.create_dropdown()
        self.create_MW_label()
        self.create_mass_entry()
        self.create_eq_label()

    # Creates a label stating if the chemical is the limiting reactant or not
    def set_kind_label(self):
        if self.limiting == False:
            kind_label = 'Reagent'
        elif self.limiting == True:
            kind_label = 'Limiting reactant'

        ttk.Label(self, text = kind_label).grid(column = 0, row = 0, padx = PAD_X, pady = PAD_Y)

    # Creates dropdown menu for selecting chemical
    def create_dropdown(self):
        self.selection_var = tk.StringVar()
        self.selection_dropdown = ttk.Combobox(self, textvariable = self.selection_var, state = 'readonly')
        self.selection_dropdown['values'] = list(CHEMICALS.keys())
        self.selection_dropdown.grid(column = 1, row = 0, padx = PAD_X, pady = PAD_Y)
        self.selection_dropdown.bind('<<ComboboxSelected>>', lambda event: self.update_MW_label())
        
    # Creates label displaying molecular weight
    def create_MW_label(self):
        self.selection_MW_label = ttk.Label(self, text = 'No chemical selected')
        self.selection_MW_label.grid(column = 1, row = 1, padx = PAD_X, pady = PAD_Y)


    # Updates molecular weight label, called when a chemical is selected from the dropdown menu
    def update_MW_label(self):
        updated_MW = CHEMICALS[self.selection_var.get()]['MW']
        self.selection_MW_label.config(text = f'{updated_MW} g/mol')

    # Entry for mass
    def create_mass_entry(self):
        self.mass_var = tk.StringVar()
        self.mass_entry = ttk.Entry(self, textvariable = self.mass_var)
        self.mass_entry.grid(column = 2, row = 0, padx = PAD_X, pady = PAD_Y)
        ttk.Label(self, text = 'mg').grid(column = 2, row = 1, padx = PAD_X, pady = PAD_Y)

    def create_eq_label(self):
        ttk.Label(self, text = '1 eq.').grid(column = 3, row = 0, padx = PAD_X, pady = PAD_Y)
        


