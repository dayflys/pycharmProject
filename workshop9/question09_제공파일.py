import pandas as pd
import numpy as np

df = pd.read_csv('data/employee_sample.csv', index_col=0)
# print(df)
### 코드 구현 ######
df['SCORE'] = 100
df.loc[['Niko','Penelope','Aria'],"SCORE"] = [3,6,4]
print(df)
### 코드 구현 ######