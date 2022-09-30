'''
    인덱스 관리2
        기존 인덱스를 재배치
            new_df = df.reindex(재배치 인덱스 값 리스트)

'''

import pandas as pd
import numpy as np

list_value = np.arange(15).reshape(5,3)
df = pd.DataFrame(list_value)
print(df)

'''
    0   1   2
0   0   1   2
1   3   4   5
2   6   7   8
3   9  10  11
4  12  13  14
'''
df = pd.DataFrame(list_value, columns=['x','y','z'], index=list('EDABC'))
print(df)

new_df = df.reindex(list("ABCDE")) #=> inplace 값이 없다.
print(new_df)
'''
    x   y   z
A   6   7   8
B   9  10  11
C  12  13  14
D   3   4   5
E   0   1   2
'''


'''
    x   y   z
E   0   1   2
D   3   4   5
A   6   7   8
B   9  10  11
C  12  13  14
'''

