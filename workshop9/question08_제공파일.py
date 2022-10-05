import pandas as pd
import numpy as np

df = pd.read_csv('data/employee_sample.csv', index_col=0)
# print(df)
### 코드 구현 ######
df["FLOOR"] = np.random.randint(1,10,size=20)[:7]
df['LAST NAME'] = pd.Series(["Smith",'Jones','Williams','Green','Brown','Simpson','Peters'],index=df.index)
df['BONUS'] = df["FLOOR"]* df['SALARY']
print(df)
### 코드 구현 ######