import pandas as pd
import numpy as np

df = pd.read_csv('data/employee_sample.csv', index_col=0)
# print(df)
### 코드 구현 ######
new_df = df.assign(BONUS= [10000 if num >10 else 0 for num in df['YEARS EXPERIENCE']])
new_df = new_df.assign(Total=lambda x: (x['SALARY']*1.1+x['BONUS']))
print(new_df)

### 코드 구현 ######
