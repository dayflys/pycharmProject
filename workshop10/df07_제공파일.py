

import numpy as np
import pandas as pd
from datetime import datetime

### 코드 구현 ######
np.random.seed(123456)
df = pd.DataFrame({'foo':np.random.random(5), 'bar':range(10, 15)}, index=pd.date_range(datetime.now(), periods=5, freq='D'))
print(df.head())

### 코드 구현 ######



