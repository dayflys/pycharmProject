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

    4. 중복 조회 및 중복 제거

       df.duplicated(subset=[컬럼])
      ==> 행을 중복 검사한다.

       df.drop_duplicates()

'''

import numpy as np
import pandas as pd

df = pd.DataFrame({"k1":["one"]*3 + ["two"] * 4,
                    "k2":[1,1,2,3,3,4,4]})
print(df)
'''
k1  k2
0  one   1
1  one   1
2  one   2
3  two   3
4  two   3
5  two   4
6  two   4
'''
print("1. df에 중복된 행이 있냐")
print(df.duplicated())
'''
0    False
1     True
2    False
3    False
4     True
5    False
6     True
dtype: bool
'''
print(df.duplicated(subset=['k1']))
'''
0    False
1     True
2     True
3    False
4     True
5     True
6     True
dtype: bool
'''
print("2. 중복된 행 제거")
new_df = df.drop_duplicates(ignore_index=True)
print(new_df)