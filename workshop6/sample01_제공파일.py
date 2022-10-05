

import pandas as pd
import numpy as np

df = pd.read_csv('data/sample_data.csv', index_col=0)
# print(df)
### 코드 구현 ######
print(df.index)
print(df.columns)
print(df.to_numpy())
### 코드 구현 ######
