'''

    DataFrame 컬럼 및 인덱스 변경

    1. 컬럼 변경

        df.columns= [값, 값2, 값3, ...]

    2.  인덱스 변경 1

        df.index = [값,값2, 값3, ... ]

        인덱스 변경 2

        pd.DataFrame(dict_value, index=[값,값2, 값3, ... ])

'''


import pandas as pd
import numpy as np

#1. dict 이용 => 컬럼별 데이터의 갯수가 동일해야한다.
dict_value =   {'c1': [4,5,6]
                ,'c2': [14,35,26]
                ,'c3': [43,50,61]}
df = pd.DataFrame(dict_value)
print(df)
'''
   c1  c2  c3
0   4  14  43
1   5  35  50
2   6  26  61
'''
print('1. 컬럼명 변경')
df.columns = ['col1','col2','col3']
print(df)
'''
1. 컬럼명 변경
   col1  col2  col3
0     4    14    43
1     5    35    50
2     6    26    61
'''
dict_value =   {'c1': [4,5,6]
                ,'c2': [14,35,26]
                ,'c3': [43,50,61]}
df = pd.DataFrame(dict_value)

print('2. 인덱스 변경') #인덱스 기본은 0,1,2,... 등등 이다.
df.index = ['a','b','c']
print(df)


dict_value =   {'c1': [4,5,6]
                ,'c2': [14,35,26]
                ,'c3': [43,50,61]}
df = pd.DataFrame(dict_value, index=['a','b','c'])
print(df)

'''
   c1  c2  c3
a   4  14  43
b   5  35  50
c   6  26  61
'''