import subprocess

def export_pdf(reactants):

    typst_content = '''
#set text(12pt, font: "New Computer Modern Sans")
#table(columns: 5,
[*Chemical*], [*Mass (mg)*], [*Volume (mL)*], [*Amount of substance (mmol)*], [*Equivalents*],
'''

    for reactant in reactants:
        
        name = reactant
        m = reactants[reactant]['mass']
        v = reactants[reactant]['volume']
        n = reactants[reactant]['amount']
        eq = reactants[reactant]['eq']

        row = f'\n[{name}], [{m}], [{v}], [{n}], [{eq}], '
        typst_content = typst_content + row

    typst_content = typst_content + ')'

    with open('output.typ', 'w') as f:
        f.write(typst_content)

    subprocess.run(['typst', 'c', 'output.typ'])



    



experiment = {
    'DIPEA': {
        'mass': 100,
        'volume': 0.1,
        'amount': 0.3,
        'eq': 1
    },

    '3-Iodoanisole': {
        'mass': 200,
        'volume': 'N/A',
        'amount': 0.6,
        'eq': 2
    }
}

