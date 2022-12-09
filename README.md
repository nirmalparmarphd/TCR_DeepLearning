# TCR_DeepLearning
Artificial Neural Network (ANN) to predict the Thermal Contact Resistance (TCR) in metalic composite pairs with the thermal interface material. 

# Minimum Working Example
MWE of ANN model to predict a temperature drop across a metalic composite pair mentioned below4

```python:
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
```

Example Output

```
StandardScaler was fitted with feature names
  warnings.warn(
----------------------------------------------------------------------
 This is ANN model trained to predict a 'Interfacial Temperature Difference - d(Ti) [C]' and a 'Total Temperature Difference - d(T) [C]' due to the Thermal Contact Resistence (TCR) accros different metalic composite pairs.

        # for prediction
        >>> prediction = tcr_prediction(data)

        # for help
        >>> prediction.help()

        # for prediction at without pressurised condition (wop)
        >>> prediction.wop()

        # for prediction at pressurised condition (wp)
        >>> prediction.wp()

----------------------------------------------------------------------
1/1 [==============================] - 0s 135ms/step
Prediction Results:
----------------------------------------------------------------------
   TCR-Pairs  Pressure  T1[C]  T1i[C]  Prediction-d(Ti)  Prediction-d(T)
0          1         0     40      37          9.252697         6.284587
----------------------------------------------------------------------
```