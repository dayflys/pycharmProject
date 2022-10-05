

import pandas as pd
import numpy as np

df = pd.read_csv('data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
print(df[(5<=df.answercount) & (df.answercount <= 10) & (df.viewcount <1000 )].head(5))

### 코드 구현 ######