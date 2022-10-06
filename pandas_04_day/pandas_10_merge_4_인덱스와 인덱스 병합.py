import pandas as pd

'''

    merge

    1. 컬럼 vs 컬럼

    2. 컬럼 vs 인덱스
        1. pd.merge(df1,df2, left_on="df1.컬럼", right_on="df2.인덱스")
        2. pd.merge(df1,df2, left_on="df2.컬럼", right_on="df1.인덱스")
        
        3. pd.merge(df1,df2, left_on="df1.컬럼명", right_index=True) ==> 1번과 동일한 결과 출력
        4. pd.merge(df1,df2, left_index=True, right_on='df2.컬럼명') ==> 2번과 동일한 결과 출력
    
    3. 인덱스 라벨 vs 인덱스 라벨
        1. pd.merge(df1,df2, left_on="df1.index", right_on="df2.인덱스")
        2. pd.merge(df1,df2, left_on="df1.index", right_index=True)
        3. pd.merge(df1,df2, left_index=True, right_on="df2.인덱스")
        4. pd.merge(df1,df2, left_index=True, right_index=True)
    
        
        
'''
df1 = pd.DataFrame({'key':['a','b','a','a','b','c'],
                    'value':range(6)}, index=list("KBSMVC"))
df2 = pd.DataFrame({'g_value':[3.5,7]}, index=['K','S'])
print(df1)
'''
  key  value
K   a      0
B   b      1
S   a      2
M   a      3
V   b      4
C   c      5
'''
print(df2)
'''
   g_value
K      3.5
S      7.0
'''
new_df = pd.merge(df1,df2, left_on=df1.index, right_on=df2.index)
print(new_df)
'''
  key_0 key  value  g_value
0     K   a      0      3.5
1     S   a      2      7.0
'''

new_df = pd.merge(df1,df2, left_on=df1.index, right_index=True)
print(new_df)
'''
  key_0 key  value  g_value
K     K   a      0      3.5
S     S   a      2      7.0
'''
new_df = pd.merge(df1,df2, left_index=True, right_on=df2.index)
print(new_df)
'''
  key_0 key  value  g_value
K     K   a      0      3.5
S     S   a      2      7.0
'''
new_df = pd.merge(df1,df2, left_index=True, right_index=True)
print(new_df)
'''
  key  value  g_value
K   a      0      3.5
S   a      2      7.0
'''
df1 = pd.DataFrame({'x1': ['A','B','C'],
                    'x2': [1,2,3]})
df2 = pd.DataFrame({'x1': ['A','B','C'],
                    'x2': [1,2,3]})
print(df1)
'''
  x1  x2
0  A   1
1  B   2
2  C   3
'''
print(df2)
'''
  x1  x2
0  A   1
1  B   2
2  C   3
'''
new_df = pd.merge(df1,df2,on='x1')
print(new_df)
'''
  x1  x2_x  x2_y
0  A     1     1
1  B     2     2
2  C     3     3
'''
new_df = pd.merge(df1,df2,on='x1',suffixes=['_a','_b'])
print(new_df)
'''
  x1  x2_a  x2_b
0  A     1     1
1  B     2     2
2  C     3     3
'''