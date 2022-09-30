'''
    인덱스 관리3
        -> 두개의 dataframe을 병합할 시 기존 인덱스를 가져가서 행병합이 진행되기 때문에
            병합시 인덱스 세팅을 다시 해주어야 한다.
        -> 인덱스를 무시하고 데이터를 병합하면 인덱스 값이 다시 세팅이 되기 때문에 원하는 결과를 얻을 수 있다.
            =>ignore_index =True

    병합시 인덱스를 빼고 병합한다. ==> 뺀 이유는 중복해서 설정 되기 때문에
        => ignore_index = True
'''

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'age':[1,2,3]})
df2 = pd.DataFrame({'age':[4,5,6]})
print(df1)
'''
   age
0    1
1    2
2    3
'''
print(df2)
'''
   age
0    4
1    5
2    6
'''
new_df = pd.concat([df1,df2])
print(new_df)
'''
   age
0    1
1    2
2    3
0    4
1    5
2    6
'''
new_df = pd.concat([df1,df2], ignore_index=True)
print(new_df)
'''
   age
0    1
1    2
2    3
3    4
4    5
5    6
'''