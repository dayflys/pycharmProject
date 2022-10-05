'''
    널(null) 값 삭제

    1. 행 삭제

        df.dropna( axis=0, inplace=False, how=any|all )

    how = all 의 의미는 모든 행값이 null인 경우에만 삭제
    how = any 의 의미는 하나라도 행값이 null인 경우 삭제

    2. 열 삭제

        df.dropna( axis=1, inplace=False, how=any|all )

    how = all 의 의미는 모든 열값이 null인 경우에만 삭제
    how = any 의 의미는 하나라도 열값이 null인 경우 삭제
'''

import pandas as pd
import numpy as np

dict_value =   {'c1': [4,5,6,np.nan,1,np.nan]
                ,'c2': [14,35,26,4,np.nan,np.nan]
                ,'c3': [np.nan,221,43,50,61,np.nan]
                ,'c4': [np.nan,221,43,50,61,np.nan]}
df = pd.DataFrame(dict_value, index=list("ABCDEF"))
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
print("1. null이 하나라도 있으면 행 삭제")
new_df = df.dropna(axis=0, inplace=False, how='any')
print(new_df)
'''
1. null이 하나라도 있으면 행 삭제
    c1    c2     c3     c4
B  5.0  35.0  221.0  221.0
C  6.0  26.0   43.0   43.0
'''
dict_value =   {'c1': [4,5,6,np.nan,np.nan]
                ,'c2': [14,35,26,4,np.nan]
                ,'c3': [np.nan,221,43,50,np.nan]}
df = pd.DataFrame(dict_value, index=list("ABCDE"))
print(df)
'''
    c1    c2     c3
A  4.0  14.0    NaN
B  5.0  35.0  221.0
C  6.0  26.0   43.0
D  NaN   4.0   50.0
E  NaN   NaN    NaN
'''
print("2. 모든 행이 null이면 행 삭제")
new_df = df.dropna(axis=0, inplace=False, how='all')
print(new_df)
'''
    c1    c2     c3
A  4.0  14.0    NaN
B  5.0  35.0  221.0
C  6.0  26.0   43.0
D  NaN   4.0   50.0
'''
#######################
dict_value =   {'c1': [4,5,6,np.nan,np.nan]
                ,'c2': [14,35,26,4,45]
                ,'c3': [np.nan,221,43,50,np.nan]
                ,'c4': [np.nan,np.nan,np.nan,np.nan,np.nan]}
df = pd.DataFrame(dict_value, index=list("ABCDE"))
print(df)
'''
    c1  c2     c3  c4
A  4.0  14    NaN NaN
B  5.0  35  221.0 NaN
C  6.0  26   43.0 NaN
D  NaN   4   50.0 NaN
E  NaN  45    NaN NaN
'''
print("1. null이 하나라도 있으면 열 삭제")
new_df = df.dropna(axis=1, inplace=False, how='any')
print(new_df)
'''
1. null이 하나라도 있으면 열 삭제
   c2
A  14
B  35
C  26
D   4
E  45
'''
print("2. 모든 열이 null이면 열 삭제")
new_df = df.dropna(axis=1, inplace=False, how='all')
print(new_df)
'''
    c1  c2     c3
A  4.0  14    NaN
B  5.0  35  221.0
C  6.0  26   43.0
D  NaN   4   50.0
E  NaN  45    NaN
'''