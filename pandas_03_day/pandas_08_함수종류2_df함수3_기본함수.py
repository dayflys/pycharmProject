'''

    기본 함수
    1. 값 변경
      df.replace({old:new, old:new})
      df.replace({컬럼명:[old,old,.], 컬럼명:old}, new)

    2. 컬럼/인덱스 라벨명 변경
      df.rename(columns={ } )
      df.rename(index={ } )

    3. all, any
    * null 값 표현 방법?  np.nan, pd.NA , None ==> True로 처리된다.
      pandas의 false 처리는 "", 0, []

'''

import numpy as np
import pandas as pd

dict_value = {"c":[4,5,6, np.nan, None],
              "a":[14,35,26,4, 33],
              "b":[300,221, 43,50,61]}
df = pd.DataFrame(dict_value, index=list("BECAD"))
print(df)
'''
    c   a    b
B  4.0  14  300
E  5.0  35  221
C  6.0  26   43
A  NaN   4   50
D  1.0  33   61
'''
print("1. 지정된 old값을 new값으로 치환 ")
new_df = df.replace({300:3, 221:2, 4:400})
print(new_df)

print("2. dict값을 임의의 값으로 변경 ")
new_df = df.replace({'c': 4.0, 'b':300}, 900)
new_df = df.replace({'c': [4.0,1.0], 'b':300}, 900)
print(new_df)

print("3. 컬럼명/index라벨명 변경 ")
new_df = df.rename(columns={"c":"C","b":"B","a":"A"})
new_df = df.rename(index={"C":"c","B":"b","A":"a","D":"d","E":"e"})
print(new_df)
'''
     c   a    b
B  4.0  14  300
E  5.0  35  221
C  6.0  26   43
A  NaN   4   50
D  1.0  33   61
'''
print("4. 모든 컬럼/행이 참이냐? ")
print(df)
print(df.all(axis=0)) # 모든 컬럼
print(df.all(axis=1)) # 모든 행

print("5. 하나라도 컬럼/행이 참이냐? ")
print(df)
print(df.any(axis=0)) # 모든 컬럼
print(df.any(axis=1)) # 모든 행


