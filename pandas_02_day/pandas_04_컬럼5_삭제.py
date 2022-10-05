'''
    DataFrame에 컬럼 삭제

   1. 단일 컬럼 삭제
    삭제된 series = df.pop('컬럼명')

    del df['컬럼명']

    2. 다중 컬럼 삭제

    df.drop(column=리스트, inplace=False)
    df.drop(리스트, inplace=False, axis=1)

'''

import pandas as pd
import numpy as np
dict_value =   {'국어': [4,5,6,7,8]
                ,'수학': [14,35,26,8,3]
                ,'영어': [4, 5, 6, 7, 8]
                ,'과학': [14, 35, 26, 8, 3]
                ,'체육': [4,5,6,7,8]
                ,'사회': [14,35,26,8,3]
                ,'IT': [14,35,26,8,3]
                }

df = pd.DataFrame(dict_value)

print("1. 단일 컬럼 삭제")
xxx = df.pop("국어")
print(df)
'''
   수학  영어  과학  체육  사회  IT
0  14   4  14   4  14  14
1  35   5  35   5  35  35
2  26   6  26   6  26  26
3   8   7   8   7   8   8
4   3   8   3   8   3   3
'''
print(xxx)
'''
0    4
1    5
2    6
3    7
4    8
Name: 국어, dtype: int64
'''

print("2. 단일 컬럼 삭제")
del df["수학"]
print(df)
'''
   영어  과학  체육  사회  IT
0   4  14   4  14  14
1   5  35   5  35  35
2   6  26   6  26  26
3   7   8   7   8   8
4   8   3   8   3   3
'''

print("3. 다중 컬럼 삭제")
df.drop( columns=['영어','과학'],inplace=True)
print(df)
'''
   체육  사회  IT
0   4  14  14
1   5  35  35
2   6  26  26
3   7   8   8
4   8   3   3
'''
new_df = df.drop( columns=['체육','사회']) # inplace=False 이기 때문에 삭제된 복사본이 반환되고 원본은 그대로 존재한다.
print(df)
'''
   체육  사회  IT
0   4  14  14
1   5  35  35
2   6  26  26
3   7   8   8
4   8   3   3
'''
print(new_df)
'''
   IT
0  14
1  35
2  26
3   8
4   3
'''

print("3. 다중 컬럼 삭제")
df.drop( ['체육','사회'],axis=1,inplace=True) # column를 사용안할때에는 axis=1 지정을 해야 column 삭제가 된다.
print(df)
'''
   IT
0  14
1  35
2  26
3   8
4   3
'''