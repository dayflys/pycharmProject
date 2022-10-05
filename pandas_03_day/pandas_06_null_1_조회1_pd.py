'''

    null처리
    -> .csv, .json를 읽어드리게 되면 빈 값들이 존재할텐데 이를 0으로 치환하게 되면, 데이터 셋이 측정값인 경우
    -> 수치가 변동이 커지게 된다. 따라서 null값에 양 옆, 또는 위아래 값의 평균과 같은 수치값을 넣어주면 변동을 줄일 수 있다.

    -> null 값 조회
    1. pandas 함수 이용
        pd.isna(스칼라|다차원배열|Series|데이터프레임)
        pd.isnull() == pd.isna

        ===> isnull = isna (일급객체) => 파이썬에서 함수는 데이터이므로 변수에 집어넣을 수 있다.

        *null 값 표현 방법? np.nan, pd.NA , None

        pd.notnull() => null값이 아닌 값을 조회
        pd.notnull(스칼라|다차원배열|Series|데이터프레임)

        pd.notnull = pd.notna() => 일급객체

    2. dataFrame 함수 이용
'''

import pandas as pd
import numpy as np

dict_value =   {'c1': [4,5,6,np.nan,8]
                ,'c2': [14,35,26,4,np.nan]
                ,'c3': [np.nan,221,43,50,61]}
df = pd.DataFrame(dict_value, index=list("ABCDE"))
print(df)
'''
    c1    c2     c3
A  4.0  14.0    NaN
B  5.0  35.0  221.0
C  6.0  26.0   43.0
D  NaN   4.0   50.0
E  8.0   NaN   61.0
'''
print("1. DataFrame에서 null 조회")
print(pd.isna(df))
'''
1. DataFrame에서 null 조회
      c1     c2     c3
A  False  False   True
B  False  False  False
C  False  False  False
D   True  False  False
E  False   True  False ==> null 이 아니면 false, null 이면 true 값을 반환 한다.
'''

print("2. 특정 컬럼(Series)에서 null 조회 - 단일 행 조회")
print(pd.isna(df['c2']))
'''
2. 특정 컬럼(Series)에서 null 조회
A    False
B    False
C    False
D    False
E     True
Name: c2, dtype: bool
'''
print("2. 특정 컬럼(Series)에서 null 조회 - fancy 색인 조회")
print(pd.isna(df[['c2','c3']]))
'''
      c2     c3
A  False   True
B  False  False
C  False  False
D  False  False
E   True  False
'''

print(pd.isnull(df))
'''
      c1     c2     c3
A  False  False   True
B  False  False  False
C  False  False  False
D   True  False  False
E  False   True  False
'''
print(pd.isnull(df['c2']))
'''
A    False
B    False
C    False
D    False
E     True
Name: c2, dtype: bool
'''
print(pd.isnull(df[['c2','c3']]))
'''
      c2     c3
A  False   True
B  False  False
C  False  False
D  False  False
E   True  False
'''

##############
print(pd.notnull(df))
'''
      c1     c2     c3
A   True   True  False
B   True   True   True
C   True   True   True
D  False   True   True
E   True  False   True
'''
print(pd.notna(df))
'''
      c1     c2     c3
A   True   True  False
B   True   True   True
C   True   True   True
D  False   True   True
E   True  False   True
'''