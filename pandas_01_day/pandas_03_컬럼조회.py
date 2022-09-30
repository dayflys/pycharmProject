'''
    DataFrame 조회

    1. 컬럼 조회 -selection
        -sql: select 컬럼명 , 컬럼명2 ,....
        -df:
            df.컬럼명 ===> series 반환
            df['컬럼명'] ===> series로 반환
            df[ ['컬럼명','컬럼명2','컬럼명3',...] ] ===> 다중 컬럼 조회 가능, DataFrame으로 반환


'''
import pandas as pd
import numpy as np

dict_value =   {'c1': [4,5,6]
                ,'c2': [14,35,26]
                ,'c3': [43,50,61]}
df  = pd.DataFrame(dict_value)
print(df)
'''
   c1  c2  c3
0   4  14  43
1   5  35  50
2   6  26  61
'''

print(df.c1,type(df.c1)) #series로 반환 됨
'''
0    4
1    5
2    6
Name: c1, dtype: int64 <class 'pandas.core.series.Series'>
'''

print(df['c2']) #series로 반환 됨
'''
0    14
1    35
2    26
Name: c2, dtype: int64
'''

print(df[['c1','c3']],type(df[['c1','c3']])) #DataFrame 반환
'''
   c1  c3
0   4  43
1   5  50
2   6  61 <class 'pandas.core.frame.DataFrame'> ==> dataFrame으로 반환 한다.
'''
print(df[['c3','c1']]) #DataFrame 반환
'''
   c3  c1
0  43   4
1  50   5
2  61   6
'''

#특별한 경우 ===> 동일 컬럼을 여러번 선택 가능
print(df[['c1','c1','c1','c1']]) #DataFrame 반환
'''
   c1  c1  c1  c1
0   4   4   4   4
1   5   5   5   5
2   6   6   6   6
'''