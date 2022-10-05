

import pandas as pd
import numpy as np

df = pd.read_csv('data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
print(df.loc[df.quest_name == df.ans_name,["id",'score','quest_name','ans_name']].head(7))

### 코드 구현 ######
