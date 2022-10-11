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


     5.
        df.apply(함수)
'''

import numpy as np
import pandas as pd

dict_value = {"국어":[4,5,6,7,8],
              "수학":[14,35,26,8,3],
              "영어":[43,50,61,3,56]}

df = pd.DataFrame(dict_value)
print(df)
'''
   국어  수학  영어
0   4  14  43
1   5  35  50
2   6  26  61
3   7   8   3
4   8   3  56
'''
def my_fun(x):
    return x+1

new_df = df.apply(my_fun)
new_df = df.apply(lambda x:x+1)
print(new_df)
'''
   국어  수학  영어
0   5  15  44
1   6  36  51
2   7  27  62
3   8   9   4
4   9   4  57
'''

new_df = df.apply(np.sum, axis=0)
new_df = df.apply(np.sum, axis=1)
new_df = df.apply(np.mean, axis=0)
new_df = df.apply(np.mean, axis=1)

# 응용
df["점수총합"] = df.apply(np.sum, axis=1)
df["평균"] = df.apply(np.mean, axis=1)
print("평균값이 35 이상만 출력")
print(df[df["평균"].apply(lambda x: x >= 35.0)])
'''
평균값이 35 이상만 출력
   국어  수학  영어  점수총합    평균
1   5  35  50    90  45.0
2   6  26  61    93  46.5
'''


print(df)
'''
   국어  수학  영어  점수총합    평균
0   4  14  43    61  30.5
1   5  35  50    90  45.0
2   6  26  61    93  46.5
3   7   8   3    18   9.0
4   8   3  56    67  33.5
'''
xxx = df.apply(np.sum, axis=0)
print(xxx)
'''
국어       30.0
수학       86.0
영어      213.0
점수총합    329.0
평균      164.5
dtype: float64
'''
print(xxx.to_frame().T)
'''
     국어    수학     영어   점수총합     평균
0  30.0  86.0  213.0  329.0  164.5
'''
xxx = xxx.to_frame().T
new_df = pd.concat([df, xxx], ignore_index=True)
new_df.index=[0,1,2,3,4,"과목별 총합"]
print(new_df)
'''
          국어    수학     영어   점수총합     평균
0        4.0  14.0   43.0   61.0   30.5
1        5.0  35.0   50.0   90.0   45.0
2        6.0  26.0   61.0   93.0   46.5
3        7.0   8.0    3.0   18.0    9.0
4        8.0   3.0   56.0   67.0   33.5
과목별 총합  30.0  86.0  213.0  329.0  164.5
'''


