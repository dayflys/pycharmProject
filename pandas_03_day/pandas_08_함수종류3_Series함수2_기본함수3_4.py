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

        7.
        df['컬럼'].isin(리스트)
        ==> 지정된 리스트 값이 데이터 프레임 안에 있으면 True, 없으면 False

         df['컬럼'].between(start,end)
        ==> 데이터가 start와 end사이의 값이 있으면 True, 없으면 False
        ==> start와 end값도 포함

        df['컬럼'].nunique()
            ===> unique한 갯수 반환, 데이터 종류 수를 센다 중복값은 한번만 센다.

         df['컬럼'].unique()
            ===> unique한 값을 반환, 기본적으로 nan을 포함시킴



'''

import numpy as np
import pandas as pd

dict_value = {"국어":[4,5,6,7,8],
              "수학":[14,35,26,8,3],
              "영어":[43,50,61,3,56]}

df = pd.DataFrame(dict_value)

print(df['국어'].isin([4,100,5,35]))
'''
0     True
1     True
2    False
3    False
4    False
Name: 국어, dtype: bool
'''
print(df['국어'].between(4,7)) # start,end 값을 포함한다.
'''
0     True
1     True
2     True
3     True
4    False
Name: 국어, dtype: bool
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
print(df['c'].nunique())
'''
nan 포함되지 않은 unique한 개수
3
'''
print('nan 포함된 unique한 개수')
print(df['c'].nunique(dropna=False))
'''
nan 포함된 unique한 개수
4
'''
print('nan 포함된 unique한 값')
print(df['c'].unique())
'''
nan 포함된 unique한 값
[ 1.  5.  6. nan]
'''
print('값의 빈도수 반환 - nan 제외')
print(df['c'].value_counts())
'''
값의 빈도수 반환 - nan 제외
1.0    2
5.0    1
6.0    1
Name: c, dtype: int64
'''
print(df['c'].value_counts(ascending=True,dropna=False))
'''
5.0    1
6.0    1
NaN    1
1.0    2
Name: c, dtype: int64
'''