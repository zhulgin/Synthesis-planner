import subprocess
from config import TYPST_TEMPLATE

def typst_pdf(reactants):

    typst_content = TYPST_TEMPLATE

    for reactant in reactants:
        
        name = reactant
        kind = reactants[reactant]['kind']
        m = reactants[reactant]['mass']
        v = reactants[reactant]['volume']
        n = reactants[reactant]['amount']
        eq = reactants[reactant]['eq']

        row = f'\n[{kind}], [{name}], [{m}], [{v}], [{n}], [{eq}], '
        typst_content += row

    typst_content += ')'

    with open('output.typ', 'w') as f:
        f.write(typst_content)

    subprocess.run(['typst', 'c', 'output.typ'])

