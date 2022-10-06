

import numpy as np
import pandas as pd

sp500 = pd.read_csv("./data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

print(sp500.head())
### 코드 구현 ######

sp500_copy = sp500.assign(RoundedPrice=sp500.Price.round())
### 코드 구현 ######
print(sp500_copy.head())

# 2.컬럼삽입:  df.insert(컬럼인덱스, 컬럼명, 값)
sp500_copy.insert(1, 'RoundedPrice2', sp500.Price.round() )
print(sp500_copy.head())