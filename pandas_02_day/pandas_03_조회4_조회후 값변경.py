'''
    DataFrame의 행과 컬럼 조회

    1. 라벨 조회 후 값변경
    - 기본문법은 df.loc[행라벨, 컬럼라벨] = 값
    - 행라벨 (인덱싱, fancy색인, 슬라이싱,boolean 다 가능)
    - 컬럼라벨 (인덱싱, fancy색인, 슬라이싱,boolean 다 가능)
    - 괄호 안에는 둘다 라벨이 와야 한다

    2. 위치 조회 후 값 변경
    - 기본문법은 df.loc[행위치, 컬럼위치] = 값
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
'''
    0   1   2
      c1  c2  c3
0  A   4  14  43
1  B   5  35  50
2  C   6  26  61
3  D   7   8   3
4  E   8   3  56
'''
print("1. A행값을 100으로 변경")
df.loc['A'] = 100
print(df)
'''
    c1   c2   c3
A  100  100  100
B    5   35   50
C    6   26   61
D    7    8    3
E    8    3   56
'''

print("2. B,C행값을 200으로 변경")
df.loc[['B','C']] = 200
print(df)
'''
    c1   c2   c3
A  100  100  100
B  200  200  200
C  200  200  200
D    7    8    3
E    8    3   56
'''
print("3. B,E행 c2,c3를 300으로 변경")
df.loc[['B','E'],['c2','c3']] = 300
print(df)
'''
    c1   c2   c3
A  100  100  100
B  200  300  300
C  200  200  200
D    7    8    3
E    8  300  300
'''

print("4. B~D행 c1~c2를 400으로 변경")
df.iloc[1:4,0:2] = 400
print(df)
'''
    c1   c2   c3
A  100  100  100
B  400  400  300
C  400  400  200
D  400  400    3
E    8  300  300
'''
print("5. A,C,E행 c1,c3를 500으로 변경")
df.iloc[[True,False,True,False,True],[True,False,True]] = 500
print(df)
'''
    c1   c2   c3
A  500  100  500
B  400  400  300
C  500  400  500
D  400  400    3
E  500  300  500
'''

