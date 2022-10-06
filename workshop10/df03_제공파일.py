

import numpy as np
import pandas as pd

sp500 = pd.read_csv("./data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

print(sp500.head())
### 코드 구현 ######
sp500_copy = sp500.assign(RoundedPrice=sp500.Price.round())
sp500_copy['Price']=sp500_copy['RoundedPrice']

### 코드 구현 ######
print(sp500_copy.head())