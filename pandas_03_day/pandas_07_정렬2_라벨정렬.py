'''
    정렬

    1. 컬럼 정렬 ==> sql에서 사용했던 정렬과 비슷하다. 데이터 값을 정렬

        df.sort_values()

    2. 위치값 정렬 ===> 인덱스 값이 아닌 라벨로 정렬하는 것을 이야기 함

        df.sort_index()



'''

import pandas as pd
import numpy as np

dict_value =   {'c': [4,5,6,np.nan,1]
                ,'a': [14,35,26,4,33]
                ,'b': [300,221,43,50,61]}
df = pd.DataFrame(dict_value, index=list("BECAD"))
print(df)
'''
     c   a    b
B  4.0  14  300
E  5.0  35  221
C  6.0  26   43
A  NaN   4   50
D  1.0  33   61
'''
print('1. 행 라벨로 오름차순 정렬')
new_df = df.sort_index()
print(new_df)
'''
     c   a    b
A  NaN   4   50
B  4.0  14  300
C  6.0  26   43
D  1.0  33   61
E  5.0  35  221
'''
print('2. 행 라벨로 내림차순 정렬')
new_df = df.sort_index(ascending=False)
print(new_df)
'''
     c   a    b
E  5.0  35  221
D  1.0  33   61
C  6.0  26   43
B  4.0  14  300
A  NaN   4   50
'''
print('3. 열 라벨로 오름차순 정렬')
new_df = df.sort_index(axis=1)
print(new_df)
'''
3. 열 라벨로 오름차순 정렬
    a    b    c
B  14  300  4.0
E  35  221  5.0
C  26   43  6.0
A   4   50  NaN
D  33   61  1.0
'''
print('4. 열 라벨로 내림차순 정렬')
new_df = df.sort_index(axis=1, ascending=False)
print(new_df)
'''
     c    b   a
B  4.0  300  14
E  5.0  221  35
C  6.0   43  26
A  NaN   50   4
D  1.0   61  33
'''