

import pandas as pd
import numpy as np

df = pd.read_csv('data/food_inspections.csv')
print(df.head())
### 코드 구현 ######
df = df.set_index("DBA Name")
print(df.iloc[500:506])

### 코드 구현 ######