
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
print(df[(df.ans_name == "Scott Boston") & (df.score >= 5)])

### 코드 구현 ######