'''
    DataFrame의 행과 컬럼 조회

    1. 라벨 조회
    - 기본문법은 df.loc[행라벨, 컬럼라벨]
    - 행라벨 (인덱싱, fancy색인, 슬라이싱,boolean 다 가능)
    - 컬럼라벨 (인덱싱, fancy색인, 슬라이싱,boolean 다 가능)
    - 괄호 안에는 둘다 라벨이 와야 한다

    2. 위치 조회
    - 기본문법은 df.loc[행위치, 컬럼위치]
    - 행위치 (인덱싱, fancy색인, 슬라이싱,boolean 다 가능)
    - 컬럼위치 (인덱싱, fancy색인, 슬라이싱,boolean 다 가능)
    - 괄호 안에는 둘다 위치가 와야 한다.
'''

import pandas as pd
import numpy as np

dict_value =   {'c1': [4,5,6,7,8]
                ,'c2': [14,35,26,8,3]
                ,'c3': [43,50,61,3,56]}
df  = pd.DataFrame(dict_value, index=list('ABCDE'))
print(df)
'''
    0   1   2
      c1  c2  c3
0  A   4  14  43
1  B   5  35  50
2  C   6  26  61
3  D   7   8   3
4  E   8   3  56
'''
print("1. A행 c1 컬럼", end=" ")
print(df.iloc[0,0]) #1. A행 c1 컬럼 4


print("2. A,B행 c1 컬럼", end=" ")
print(df.iloc[[0,1],0]) #2. A,B행 c1 컬럼 A    4 B    5 Name: c1, dtype: int64 => series로 도출된다.

print("3. A,C행 c1,c3 컬럼")
print(df.iloc[[0,2],[0,2]])
'''
1. A,C행 c1,c3 컬럼
   c1  c3
A   4  43
C   6  61 ==> dataframe 으로 도출된다.
'''


print("4. B~D행 c1,c3 컬럼")
print(df.iloc[1:4,[0,2]]) #=> 행위치로 조회하는 것이기 때문에 stop값이 포함 안되기 때문에 주의해야 한다
'''
4. B~D행 c1,c3 컬럼
   c1  c3
B   5  50
C   6  61
D   7   3 ==> dataframe으로 도출된다. 
'''
print("5. B~D행 c2~c3 컬럼")
print(df.iloc[1:4,1:]) #=> 행라벨로 조회하는 것이기 때문에 stop값도 포함이 된다.
'''
5. B~D행 c2~c3 컬럼
   c2  c3
B  35  50
C  26  61
D   8   3 ==> dataframe으로 도출된다.
'''

print("6. A,C,E행 c2,c3 컬럼")
dict_value =   {'c1': [4,5,6,7,8]
                ,'c2': [14,35,26,8,3]
                ,'c3': [43,50,61,3,56]}
df  = pd.DataFrame(dict_value, index=list('ABCDE'))
print(df.iloc[[True,False,True,False,True],1:3]) #=> boolean 색인 시에는 boolean 값 개수가 행라벨 수와 일치해야한다.
#일반적으로는 논리값을 반환된 연산 식을 사용한다.
'''
6. A,C,E행 c2,c3 컬럼
   c2  c3
A  14  43
C  26  61
E   3  56
'''
print("7. A,C,E행 c2,c3 컬럼")
print(df.iloc[[True,False,True,False,True],[False,True,True]])
'''
7. A,C,E행 c2,c3 컬럼
   c2  c3
A  14  43
C  26  61
E   3  56
'''

