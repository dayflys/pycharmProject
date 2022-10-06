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

    6.
        df.eval(연산식)
        -> series는 지원안됨

    7.
        df.isin(리스트)
        ==> 지정된 리스트 값이 데이터 프레임 안에 있으면 True, 없으면 False

    8. df.nunique()
    ===> unique한 갯수 반환, 데이터 종류 수를 센다 중복값은 한번만 센다.

'''

import numpy as np
import pandas as pd

dict_value = {"국어":[4,5,6,7,8],
              "수학":[14,35,26,8,3],
              "영어":[43,50,61,3,56]}

df = pd.DataFrame(dict_value)

print(df.eval('국어+수학+영어'))
'''
0    61
1    90
2    93
3    18
4    67
dtype: int64
'''
df['총합'] = df.eval('국어+수학+영어')
print(df)
'''
   국어  수학  영어  총합
0   4  14  43  61
1   5  35  50  90
2   6  26  61  93
3   7   8   3  18
4   8   3  56  67
'''
df['합격여부'] = df.eval('총합>80')
print(df)
'''
   국어  수학  영어  총합   합격여부
0   4  14  43  61  False
1   5  35  50  90   True
2   6  26  61  93   True
3   7   8   3  18  False
4   8   3  56  67  False
'''
print()
print(df.isin([4,100,50,35]))
'''
      국어     수학     영어     총합   합격여부
0   True  False  False  False  False
1  False   True   True  False  False
2  False  False  False  False  False
3  False  False  False  False  False
4  False  False  False  False  False
'''
dict_value =   {'c': [1,5,6,np.nan,1]
                ,'a': [4,np.nan,26,4,np.nan]
                ,'b': [300,np.nan,43,np.nan,61]}
df = pd.DataFrame(dict_value, index=list("BECAD"))
print(df)
'''
     c     a      b
B  1.0   4.0  300.0
E  5.0   NaN    NaN
C  6.0  26.0   43.0
A  NaN   4.0    NaN
D  1.0   NaN   61.0
'''
print('nan 포함되지 않은 unique한 개수')
print(df.nunique())
'''
c    3
a    2
b    3
dtype: int64
'''
print('nan 포함된 unique한 개수')
print(df.nunique(dropna=False))
'''
c    4
a    3
b    4
dtype: int64
'''
