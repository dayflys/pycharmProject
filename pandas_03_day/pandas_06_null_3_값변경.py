'''
    널(null) 값 치환

    df.fillna(임의값, inplace=False)
    df.fillna({컬럼명: 값, 컬럼명:값}, inplace=False)

    #null 값의 앞(forward)에 있는 값으로 채움
    df.fillna(method='ffill', inplace=False)

    #null 값의 뒤(backward)에 있는 값으로 채움
    df.fillna(method='bfill', inplace=False)

'''

import pandas as pd
import numpy as np

dict_value =   {'c1': [4,5,6,np.nan,1]
                ,'c2': [14,35,26,4,np.nan]
                ,'c3': [np.nan,221,43,50,61]}
df = pd.DataFrame(dict_value, index=list("ABCDE"))
print(df)
'''
    c1    c2     c3     c4
A  4.0  14.0    NaN    NaN
B  5.0  35.0  221.0  221.0
C  6.0  26.0   43.0   43.0
D  NaN   4.0   50.0   50.0
E  1.0   NaN   61.0   61.0
F  NaN   NaN    NaN    NaN
'''
print("1. 모든 null을 임의의 값으로 변경")
new_df = df.fillna('N/A')
print(new_df)
'''
    c1    c2     c3
A  4.0  14.0    N/A
B  5.0  35.0  221.0
C  6.0  26.0   43.0
D  N/A   4.0   50.0
E  1.0   N/A   61.0
'''
print("2. 컬럼단위로 null을 임의의 값으로 변경")
new_df = df.fillna({'c1':0,'c2':'N/A','c3':-1})
print(new_df)
'''
2. 컬럼단위로 null을 임의의 값으로 변경
    c1    c2     c3
A  4.0  14.0   -1.0
B  5.0  35.0  221.0
C  6.0  26.0   43.0
D  0.0   4.0   50.0
E  1.0   N/A   61.0
'''

dict_value =   {'c1': [4,5,6,np.nan,1]
                ,'c2': [14,np.nan,35,26,4]
                ,'c3': [221,np.nan,43,50,61]}
df = pd.DataFrame(dict_value, index=list("ABCDE"))
print(df)
'''
    c1    c2     c3
A  4.0  14.0  221.0
B  5.0   NaN    NaN
C  6.0  35.0   43.0
D  NaN  26.0   50.0
E  1.0   4.0   61.0
'''

print("3. null 값의 앞(forward)에 있는 값으로 채움")
new_df = df.fillna(method='ffill')
print(new_df)
'''
    c1    c2     c3
A  4.0  14.0  221.0
B  5.0  14.0  221.0
C  6.0  35.0   43.0
D  6.0  26.0   50.0
E  1.0   4.0   61.0
'''
print("4. null 값의 뒤(backward)에 있는 값으로 채움")
new_df = df.fillna(method='bfill')
print(new_df)
'''
4. null 값의 뒤(backward)에 있는 값으로 채움
    c1    c2     c3
A  4.0  14.0  221.0
B  5.0  35.0   43.0
C  6.0  35.0   43.0
D  1.0  26.0   50.0
E  1.0   4.0   61.0
'''
