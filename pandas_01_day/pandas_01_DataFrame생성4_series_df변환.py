'''

    series 이용

    가. series 생성
    s1 = pd.Series()
    s2 = pd.Series()

    나. DataFrame 생성
    df = pd.DataFrame([s1,s2,....])

'''

import pandas as pd
import numpy as np
s1 = pd.Series([10,20,30], name='age')
print(s1, type(s1))
'''
0    10
1    20
2    30
Name: age, dtype: int64 <class 'pandas.core.series.Series'>
'''

#series ==> df 변경
df = s1.to_frame('나이')
print(df)
'''
   나이
0  10
1  20
2  30 => name,dtype 이 나오지 않으면 dataframe 이다. 
'''