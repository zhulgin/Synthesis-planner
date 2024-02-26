import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
from chemicals import CHEMICALS




def calculate_mass():
    try:
        # Get inputs
        eq_ratio = float(equivalents_entry.get())
        limiting_reactant_mass = float(limiting_reactant_mass_entry.get())
        limiting_reactant_name = limiting_reactant_var.get()
        limiting_reactant_molar_mass = CHEMICALS[limiting_reactant_name]["MW"]


        chemical_name = chemical_var.get()
        chemical_molar_mass = CHEMICALS[chemical_name]["MW"]
        
        # Calculate mass
        mass_needed = eq_ratio * chemical_molar_mass * limiting_reactant_mass / limiting_reactant_molar_mass
        
        # Update result label
        result_label.config(text=f"Mass needed: {mass_needed:.2f} g")
    except ValueError:
        result_label.config(text="Invalid input")

# Create main window
root = tk.Tk()
root.title("Organic Synthesis Experiment Planner")
style = Style("darkly")  # Choose a Bootstrap theme

# Create frames
input_frame = ttk.Frame(root)
input_frame.pack(padx=10, pady=10)

# Add labels and entries
ttk.Label(input_frame, text="Number of Equivalents:").grid(row=0, column=0, padx=5, pady=5)
equivalents_entry = ttk.Entry(input_frame)
equivalents_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Limiting Reactant Mass (g):").grid(row=1, column=0, padx=5, pady=5)
limiting_reactant_mass_entry = ttk.Entry(input_frame)
limiting_reactant_mass_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Chemical:").grid(row=2, column=0, padx=5, pady=5)
chemical_var = tk.StringVar()
chemical_dropdown = ttk.Combobox(input_frame, textvariable=chemical_var, state="readonly")
chemical_dropdown['values'] = list(CHEMICALS.keys())
chemical_dropdown.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Limiting Reactant:").grid(row=3, column=0, padx=5, pady=5)
limiting_reactant_var = tk.StringVar()
limiting_reactant_dropdown = ttk.Combobox(input_frame, textvariable=limiting_reactant_var, state="readonly")
limiting_reactant_dropdown['values'] = list(CHEMICALS.keys())
limiting_reactant_dropdown.grid(row=3, column=1, padx=5, pady=5)

# Add button to calculate mass
calculate_button = ttk.Button(input_frame, text="Calculate Mass", command=calculate_mass)
calculate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Add result label
result_label = ttk.Label(input_frame, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Start the main loop
root.mainloop()
