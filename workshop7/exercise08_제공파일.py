

import pandas as pd
import numpy as np

df = pd.read_csv('data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
print(df[df.answercount == 5].head())

### 코드 구현 ######
