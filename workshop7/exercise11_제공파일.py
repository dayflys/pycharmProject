

import pandas as pd
import numpy as np

df = pd.read_csv('data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
print(df[(df.ans_name).isnull() & (df.score > 100)])

### 코드 구현 ######

