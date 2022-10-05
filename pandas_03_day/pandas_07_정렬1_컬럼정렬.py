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
print("1. c컬럼으로 오름차순 정렬")
new_df = df.sort_values(by='c')
print(new_df)
'''
     c   a    b
D  1.0  33   61
B  4.0  14  300
E  5.0  35  221
C  6.0  26   43
A  NaN   4   50 ==> 컬럼 C 가 정렬이 되었다.
'''
print("2. c컬럼으로 내림차순 정렬")
new_df = df.sort_values(by='c', ascending=False)
print(new_df)
'''
2. c컬럼으로 내림차순 정렬
     c   a    b
C  6.0  26   43
E  5.0  35  221
B  4.0  14  300
D  1.0  33   61
A  NaN   4   50
'''

print("3. c컬럼으로 내림차순, null값은 first정렬")
new_df = df.sort_values(by='c', ascending=False, na_position='first')
print(new_df)
'''
3. c컬럼으로 내림차순, null값은 first정렬
     c   a    b
A  NaN   4   50
C  6.0  26   43
E  5.0  35  221
B  4.0  14  300
D  1.0  33   61
'''

dict_value =   {'c': [4,6,6,np.nan,6]
                ,'a': [14,35,26,4,33]
                ,'b': [300,221,43,50,61]}
df = pd.DataFrame(dict_value, index=list("BECAD"))
print(df)
'''
     c   a    b
B  4.0  14  300
E  6.0  35  221
C  6.0  26   43
A  NaN   4   50
D  6.0  33   61
'''
print("4. c와a로 다중 컬럼정렬")
new_df = df.sort_values(by=['c','a'])
print(new_df)
'''
     c   a    b
B  4.0  14  300
C  6.0  26   43
D  6.0  33   61
E  6.0  35  221
A  NaN   4   50
'''
print("4. c와a로 다중 컬럼정렬")
new_df = df.sort_values(by=['c','a'],ascending=False)
print(new_df)
'''
     c   a    b
E  6.0  35  221
D  6.0  33   61
C  6.0  26   43
B  4.0  14  300
A  NaN   4   50
'''

