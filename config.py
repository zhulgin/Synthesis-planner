from datetime import date

APP_NAME = 'Experiment Planner'
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
DIMENSIONS = f'{1200}x{600}'
APP_ICON = 'assets/hexagon.ico'

PADX = 5
PADY = 2

KINDS = ['Reactant', 'Reagent', 'Catalyst', 'Solvent']
COL_WIDTH = 12
COL0_WIDTH = 16

BUTTON_WIDTH = 20

HELP_LABEL = 'Green = input\nBlue = output'

TYPST_TEMPLATE = f'''
#set text(12pt, font: "New Computer Modern Sans")
#set page(flipped: true, header: [Experiment {date.today()}])
#table(columns: 6,
[], [*Chemical*], [*Mass (mg)*], [*Volume (mL)*], [*Amount of substance (mmol)*], [*Equivalents*],
'''