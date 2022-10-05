'''

    기본 함수
    1. 값 변경
      df['컬럼'].replace({old:new, old:new})
      df[['컬럼','컬럼']].replace({old:new, old:new}) # inplace=False 로만 사용한다.


    2. Series name 변경
      df['컬럼'].rename("변경할 값")

    3. all, any
    * null 값 표현 방법?  np.nan, pd.NA , None ==> True로 처리된다.
      pandas의 false 처리는 "", 0, []

'''

import numpy as np
import pandas as pd

dict_value = {"c":[4,5,6, np.nan, None],
              "a":[14,35,26,4, 33],
              "b":[14,221, 43,50,61]}
df = pd.DataFrame(dict_value, index=list("BECAD"))
print(df)
'''
     c   a    b
B  4.0  14   14
E  5.0  35  221
C  6.0  26   43
A  NaN   4   50
D  NaN  33   61
'''
print("1. 특정 컬럼의 지정된 old값을 new값으로 치환 ")
# df["a"].replace({14:140, 26:260}, inplace=True)

# df[["a","b"]].replace({14:140, 26:260}, inplace=True)
# 다중 컬럼 지정할 때는 복사본(inplace=False) 형태로 수정할 것.
df = df[["a","b"]].replace({14:140, 26:260})
print(df)
'''
     a    b
B  140  140
E   35  221
C  260   43
A    4   50
D   33   61
'''
print("2. Series  name 변경 ")
print(df['a'])
'''
B    140
E     35
C    260
A      4
D     33
Name: a, dtype: int64
'''
#  Series의 name값을 변경 :  a ----> AAA
new_a = df['a'].rename("AAA") #  # scalar, changes Series.name
#  Series의 인덱스라벨 변경 :  a ----> AAA
new_a = df['a'].rename(lambda x: x+"100") # # function, changes labels
print(new_a)
'''
B100    140
E100     35
C100    260
A100      4
D100     33
Name: a, dtype: int64
'''

print("3. 특정 컬럼/행이 모두 참이냐? ")
dict_value = {"c":[4,5,6, np.nan, None],
              "a":[14,35,26,4, 0],
              "b":[14,221, 43,50,61]}
df = pd.DataFrame(dict_value, index=list("BECAD"))
print(df)
print(df)
'''
 a    b
B  140  140
E   35  221
C  260   43
A    4   50
D   0   61
'''
print(df["a"].all(axis=0)) # False
print("4. 특정 컬럼/행이 하나라도 참이냐? ")
print(df["a"].any(axis=0)) # True