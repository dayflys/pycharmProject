import pandas as pd
import numpy as np

df = pd.read_csv('data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
df.loc['Aria','DEPARTMENT'] = 'Police'
print(df)

### 코드 구현 ######

