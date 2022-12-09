# MWE minimum working example of TCR wop and wp condition
# TCR-wop "TCR at without pressurised condition"
# TCR-wp "TCR at pressurised condition"

## importing TCR ANN module
from module import *

## Data preparation
# Pair Combinations: use appropriate integer to specify the combination
    # 'Al-Br-Cu' = 1
    # 'Al-Air-Al' = 2
    # 'Al-Air-Cu' = 3
## wop or wp    
    # wop - without pressure = =
    # wp - with pressure =1
## T1 - Supply Temperature [C]
## T1i - Interfacial Temperature [C]
# data = ['Pair Combination', 'wop or wp', 'T1', 'T1i']

# example data
data = [1, 0, 40, 37]

# first load the method to predict
prediction  = tcr_prediction(data)

# for help
prediction.help()

# for wos prediction
prediction.wop()