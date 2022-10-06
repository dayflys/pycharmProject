import pandas as pd

'''

    merge

    1. 컬럼 vs 컬럼

    2. 컬럼 vs 인덱스
        1. pd.merge(df1,df2, left_on="df1.컬럼", right_on="df2.인덱스")
        2. pd.merge(df1,df2, left_on="df2.컬럼", right_on="df1.인덱스")
        
        3. pd.merge(df1,df2, left_on="df1.컬럼명", right_index=True) ==> 1번과 동일한 결과 출력
        3. pd.merge(df1,df2, left_index=True, right_on='df2.컬럼명') ==> 2번과 동일한 결과 출력
        
        
'''
df1 = pd.DataFrame({'key':['a','b','a','a','b','c'],
                    'value':range(6)})
df2 = pd.DataFrame({'group_val':[3.5,7]}, index=['a','b'])
print(df1)
'''
  key  value
0   a      0
1   b      1
2   a      2
3   a      3
4   b      4
5   c      5
'''
print(df2)
'''
   group_val
a        3.5
b        7.0
'''

new_df = pd.merge(df1, df2, left_on="key", right_on=df2.index)
print(new_df)
'''
  key  value  group_val
0   a      0        3.5
1   a      2        3.5
2   a      3        3.5
3   b      1        7.0
4   b      4        7.0
'''

new_df = pd.merge(df1, df2, left_on="key",  right_index=True)
print(new_df)
'''
  key  value  group_val
0   a      0        3.5
2   a      2        3.5
3   a      3        3.5
1   b      1        7.0
4   b      4        7.0
'''
new_df = pd.merge(df2, df1, left_index=True,  right_on='key')
print(new_df)
'''
   group_val key  value
0        3.5   a      0
2        3.5   a      2
3        3.5   a      3
1        7.0   b      1
4        7.0   b      4
'''