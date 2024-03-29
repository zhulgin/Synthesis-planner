# Import external packages
import tkinter as tk
import ttkbootstrap as tb
# Import constants from config file
from config import *
# Import chemicals dictionary
from chemicals import CHEMICALS


class Reactant(tb.Frame):
    def __init__(self, parent, kind = 'Reactant'):
        super().__init__(master = parent)
        
        self.kind = kind
        # Create labels
        self.create_kind_dropdown()
        self.create_MW_label()
        self.create_eq_entry()
        self.create_state_label()

        # Create entries and dropdown
        self.create_dropdown()
        self.create_mmol_entry()
        self.create_mass_entry()
        self.create_volume_entry()
        
    # Creates a label stating if the chemical is the limiting reactant or not
    def create_kind_dropdown(self):

        self.kind_var = tk.StringVar()
        self.kind_dropdown = tb.Combobox(self, 
            textvariable = self.kind_var, 
            state = 'readonly', 
            width = COL0_WIDTH - 2)
        
        self.kind_dropdown['values'] = KINDS
        self.kind_dropdown.grid(
            column = 0, row = 0, 
            padx = PADX, pady = PADY,
            sticky = 'w')

    # Creates label displaying molecular weight of selected chemical
    def create_MW_label(self):
        self.selection_MW_label = tb.Label(self, 
            text = 'No chemical selected')
        self.selection_MW_label.grid(
            column = 1, row = 1, 
            padx = PADX, pady = PADY,
            sticky = 'w')

    # Label displaying eq of selected chemical
    def create_eq_entry(self):
        self.eq_var = tk.StringVar()
        self.eq_entry = tb.Entry(self, 
            textvariable = self.eq_var, 
            style = 'success.TEntry', 
            width = COL_WIDTH)
        self.eq_entry.grid(
            column = 5, row = 0, 
            padx = PADX, pady = PADY,
            sticky = 'w')
        tb.Label(self, 
            text = EQ_DESC, 
            width = COL_WIDTH).grid(
                column = 5, row = 1, 
                padx = PADX, pady = PADY,
                sticky = 'w')

    # Label displaying state of selected chemical
    def create_state_label(self):
        self.selection_state_label = tb.Label(self, 
            text = '', 
            width = COL_WIDTH)
        self.selection_state_label.grid(
            column = 1, row = 2, 
            padx = PADX, pady = PADY,
            sticky = 'w')

    # Creates dropdown menu for selecting chemical
    def create_dropdown(self):
        self.selection_var = tk.StringVar()
        self.selection_dropdown = tb.Combobox(self, textvariable = self.selection_var, state = 'readonly', width = COL_WIDTH + 10)
        self.selection_dropdown['values'] = list(CHEMICALS.keys())
        self.selection_dropdown.grid(
            column = 1, row = 0, 
            padx = PADX, pady = PADY,
            sticky = 'w')
        self.selection_dropdown.bind('<<ComboboxSelected>>', lambda event: self.update())
        
    # Entry for mass
    def create_mass_entry(self):
        self.mass_var = tk.StringVar()
        self.mass_entry = tb.Entry(self, 
            textvariable = self.mass_var, 
            state = 'disabled', 
            style = 'info.TEntry', 
            foreground = 'white', 
            width = COL_WIDTH)
        self.mass_entry.grid(
            column = 2, row = 0, 
            padx = PADX, pady = PADY,
            sticky = 'w')
        tb.Label(self, 
            text = MASS_DESC, 
            width = COL_WIDTH).grid(
                column = 2, row = 1, 
                padx = PADX, pady = PADY,
                sticky = 'w')

    # Entry for volume
    def create_volume_entry(self):
        self.volume_var = tk.StringVar()
        self.volume_entry = tb.Entry(self, textvariable = self.volume_var, state = 'disabled', style = 'info.TEntry', foreground = 'white', width = COL_WIDTH)
        self.volume_entry.grid(
            column = 3, row = 0, 
            padx = PADX, pady = PADY,
            sticky = 'w')
        tb.Label(self, text = VOLUME_DESC, width = COL_WIDTH).grid(
            column = 3, row = 1, 
            padx = PADX, pady = PADY,
            sticky = 'w')


    # Entry for amount of substance. (Always disabled, just output)
    def create_mmol_entry(self):
        self.mmol_var = tk.StringVar()
        self.mmol_entry = tb.Entry(self, textvariable = self.mmol_var, state = 'disabled', style = 'info.TEntry', foreground = 'white', width = COL_WIDTH)
        self.mmol_entry.grid(
            column = 4, row = 0, 
            padx = PADX, pady = PADY,
            sticky = 'w')
        tb.Label(self, text = AMOUNT_DESC, width = COL_WIDTH).grid(
            column = 4, row = 1, 
            padx = PADX, pady = PADY,
            sticky = 'w')

    # Updates molecular weight label, called when a chemical is selected from the dropdown menu
    def update(self):
        updated_MW = CHEMICALS[self.selection_var.get()]['MW']
        self.selection_MW_label.config(text = f'{updated_MW} g/mol')
    
        

    

    

    

    
        
        


