from datetime import date

APP_NAME = 'Experiment Planner'
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
DIMENSIONS = f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}'
APP_ICON = 'assets/hexagon.ico'

PADX = 5
PADY = 2

KINDS = ['Reactant', 'Reagent', 'Catalyst', 'Solvent']
COL_WIDTH = 16
COL0_WIDTH = 16

BUTTON_WIDTH = 20

HELP_LABEL = 'Green = input\nBlue = output'

TYPST_HEADER = f'''
#set text(12pt, font: "New Computer Modern Sans")
#set page(flipped: true, header: [Experiment {date.today()}])
#table(columns: 6,
[], [*Chemical*], [*Mass (mg)*], [*Volume (mL)*], [*Amount of substance (mmol)*], [*Equivalents*],
'''

TXT_HEADER = f'''
Experiment {date.today()}

Kind\tChemical\tMass (mg)\tVolume (mL)\tAmount of substance (mmol)\tEquivalents
'''

MASS_DESC = 'Mass (mg)'
VOLUME_DESC = 'Volume (mL)'
AMOUNT_DESC = 'Amount of\nsubstance\n(mmol)'
EQ_DESC = 'Equivalents'