import subprocess
from config import TYPST_HEADER, TXT_HEADER

def export_pdf(reactants):
    typst_content = TYPST_HEADER
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

def export_txt(reactants):
    txt_content = TXT_HEADER
    for reactant in reactants:
        name = reactant
        kind = reactants[reactant]['kind']
        m = reactants[reactant]['mass']
        v = reactants[reactant]['volume']
        n = reactants[reactant]['amount']
        eq = reactants[reactant]['eq']
        row = f'\n{kind}\t{name}\t{m}\t{v}\t{n}\t{eq}'
        txt_content += row
    with open('output.txt', 'w') as f:
        f.write(txt_content)
