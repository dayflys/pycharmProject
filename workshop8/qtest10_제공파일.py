
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
print(df.loc[df.viewcount>20000,["creationdate",'viewcount','ans_name']].head(10))

### 코드 구현 ######