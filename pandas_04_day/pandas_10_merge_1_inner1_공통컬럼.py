'''

    pandas의 병합(sql의 조인 기능) --> 기본은 inner
    1. inner 병합
        가. 공통 컬럼 존재하는 경우
            new_df = pd.merge(df,df2, on=공통컬럼)
        나. 공통 컬럼이 없는 경우
    2. outer 병합 --> outer== full outer 병합을 의미함

'''
import pandas as pd

df1 = pd.DataFrame({'x1': ['A','B','C'],
                    'x2': [1,2,3]})
df2 = pd.DataFrame({'x1': ['A','B','D'],
                    'x3': ['T',"F",'T'],
                    'x4': ['T1','F1','T1']})
print(df1)
'''
  x1  x2
0  A   1
1  B   2
2  C   3
'''
print(df2)
'''
  x1 x3  x4
0  A  T  T1
1  B  F  F1
2  D  T  T1
'''
new_df = pd.merge(df1,df2, on="x1")
print(new_df)
'''
  x1  x2 x3  x4
0  A   1  T  T1
1  B   2  F  F1
'''
new_df = pd.merge(df1['x1'],df2[['x1','x3']], on="x1") #특정 컬럼만을 병합 시킬 수도 있다. 이때 색인을 사용한다.
print(new_df)
'''
  x1 x3
0  A  T
1  B  F
'''
new_df = pd.merge(df1,df2, on="x1", indicator=True) #기본이 false 이다.
print(new_df)
'''
  x1  x2 x3  x4 _merge
0  A   1  T  T1   both
1  B   2  F  F1   both ==> both는 inner 조인을 의미 한다. 결과는 dataframe으로 도출 된다. 따라서 dataframe의 함수들을 사용할 수 있다.
'''
new_df = pd.merge(df1,df2, on="x1", indicator=True)\
        .drop(columns=['_merge'])\
        .rename(columns={'x4': 'X4'}) #\ ==> 연결 연산자
print(new_df)
'''
  x1  x2 x3  X4
0  A   1  T  T1
1  B   2  F  F1
'''

