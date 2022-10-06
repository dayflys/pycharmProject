'''

    pandas의 병합(sql의 조인 기능) --> 기본은 inner
    1. inner 병합
        가. 공통 컬럼 존재하는 경우
            new_df = pd.merge(df,df2, on=공통컬럼)
        나. 공통 컬럼이 없는 경우
            new_df = pd.merge(df,df2, left_on=df컬럼,right_on=df2컬럼)
    2. outer 병합 --> outer== full outer 병합을 의미함

'''
import pandas as pd

df1 = pd.DataFrame({'x1': ['A','B','C'],
                    'x2': [1,2,3]})
df2 = pd.DataFrame({'y1': ['A','B','D'],
                    'x3': ['T',"F",'T']
                    })
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
new_df = pd.merge(df1,df2, left_on="x1",right_on='y1')
print(new_df)
'''
  x1  x2 y1 x3
0  A   1  A  T
1  B   2  B  F
'''
new_df = pd.merge(df1,df2, left_on="x1",right_on='y1').drop(columns=['y1'])
print(new_df)
'''
  x1  x2 x3
0  A   1  T
1  B   2  F
'''
new_df = pd.merge(df1,df2, left_on="x1",right_on='y1').drop(columns=['y1']).rename(columns={'x1':'x1_y1'})
print(new_df)
'''
  x1_y1  x2 x3
0     A   1  T
1     B   2  F
'''
