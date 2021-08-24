import numpy as np
import pandas as pd

url = "https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv"
fuel_data = pd.read_csv(url, error_bad_lines=False)
fuel_data.describe(include='all')

#fuel_unit missing data

fuel_data.groupby('fuel_unit')['fuel_unit'].count()
fuel_unit
bbl        7998
gal          84
gramsU      464
kgU         110
mcf       11354
mmbtu       180
mwdth        95
mwhth       100
ton        8958
Name: fuel_unit, dtype: int64 #result = mcf, Total: 180, Percentage: 0.6%

#fuel type code
fuel_data.groupby('fuel_type_code_pudl')['fuel_type_code_pudl'].count()
fuel_type_code_pudl
coal        8547
gas        11486
nuclear      818
oil         8064
other        167
waste        441
Name: fuel_type_code_pudl, dtype: int64 # waste has the lowest