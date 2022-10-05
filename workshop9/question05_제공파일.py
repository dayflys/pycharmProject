import pandas as pd
import numpy as np

df = pd.read_csv('data/employee_sample.csv', index_col=0)
# print(df)
### 코드 구현 ######
df['SALARY'] = [df['SALARY'].iloc[a]+10000 if x == 'White' and y == "Engineering" else df['SALARY'].iloc[a] for a,(x,y) in enumerate(df[['RACE','DEPARTMENT']].values)]
df['SALARY'] = [df['SALARY'].iloc[a]+20000 if x == 'Black' and y == "Parks & Recreation" else df['SALARY'].iloc[a] for a,(x,y) in enumerate(df[['RACE','DEPARTMENT']].values)]
print(df)

### 코드 구현 ######

