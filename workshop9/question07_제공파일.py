import pandas as pd
import numpy as np

df = pd.read_csv('data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######

df['SCORE'] = [99,99,99,99,99,99,99 ]
df["BONUS RATE"] = [0.20,0.10,0.00,0.15,0.12,0.30,0.05]
print(df)
### 코드 구현 ######