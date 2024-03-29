# MW: Molecular weight in g/mol (= mg/mmol)
# density: g/mL. Set to None for solids as it will not be relevant.

CHEMICALS_unsorted = {

    'DIPEA': {
        'MW': 129.247,
        'state': 'l',
        'density': 0.742
    },

    '3-Ethynylanisole': {
        'MW': 132.16,
        'state': 'l',
        'density': 1.04
    },

    '3-Iodoanisole': {
        'MW': 234.03,
        'state': 'l',
        'density': 1.965
    },

    'LiAlH4': {
        'MW': 37.95,
        'state': 's',
        'density': None
    },

    'Pd(PPh3)4': {
        'MW': 1155.59,
        'state': 's',
        'density': None
    },

    'NaBH4': {
        'MW': 37.83,
        'state': 's',
        'density': None
    },

    'Tetrachlorocyclopropene': {
        'MW': 177.83,
        'state': 'l',
        'density': 1.45
    },

    '4-Nitrophenylchloroformate': {
        'MW': 201.56,
        'state': 's',
        'density': None
    },

    'Pyridine': {
        'MW': 79.10,
        'state': 'l',
        'density': 0.9819
    },

    '4-tert-Butylphenol': {
        'MW': 150.22,
        'state': 's',
        'density': None
    },

    'Methyl 3-(bromomethyl)benzoate': {
        'MW': 229.07,
        'state': 's',
        'density': None
    },

}

CHEMICALS = {key: value for key, value in sorted(CHEMICALS_unsorted.items())}