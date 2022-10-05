
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
print(df.loc[(30 <= df.favoritecount) & (df.favoritecount<=40),'title'::3].head())


### 코드 구현 ######