'''

    기본 함수
        기본 함수
    1. 값 변경
      df['컬럼'].replace({old:new, old:new})
      df[['컬럼','컬럼']].replace({old:new, old:new}) # inplace=False 로만 사용한다.


    2. Series name 변경
      df['컬럼'].rename("변경할 값")

    3. all, any
    * null 값 표현 방법?  np.nan, pd.NA , None ==> True로 처리된다.
      pandas의 false 처리는 "", 0, []


    4. 중복 조회 및 중복 제거

       df["컬럼"].duplicated(subset=[컬럼])
      ==> 행을 중복 검사한다.

       df["컬럼"].drop_duplicates()

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
print("1. k1에 중복된 행이 있냐")
print(df["k1"].duplicated())
'''
0    False
1     True
2     True
3    False
4     True
5     True
6     True
Name: k1, dtype: bool
'''
print("2. k1에 중복된 행 제거")
new_df = df["k1"].drop_duplicates()
print(new_df)