import pandas as pd
import numpy as np

df = pd.read_csv('data/employee_sample.csv', index_col=0)
# print(df)
### 코드 구현 ######
df['BONUS'] = [21592,3034,0,6542,3135,10077,1878]
df["UPDATE BONUS"] = [df['BONUS'].iloc[a]+5000 if x == 'Engineering' else df['BONUS'].iloc[a] for a,x in enumerate(df['DEPARTMENT'])]

print(df)
### 코드 구현 ######