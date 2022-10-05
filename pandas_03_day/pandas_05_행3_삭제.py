'''
    DataFrame에 컬럼 삭제

   1. 단일/다중 삭제

   df.drop(index=리스트, inplace=False)
   df.drop(리스트, inplace=False, axis=0)
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

df = pd.DataFrame(dict_value, index=list("ABCDE"))
print(df)
'''
   국어  수학  영어  과학  체육  사회  IT
A   4  14   4  14   4  14  14
B   5  35   5  35   5  35  35
C   6  26   6  26   6  26  26
D   7   8   7   8   7   8   8
E   8   3   8   3   8   3   3
'''
df.drop(index=['A','B'], inplace=True)
print(df)
'''
   국어  수학  영어  과학  체육  사회  IT
C   6  26   6  26   6  26  26
D   7   8   7   8   7   8   8
E   8   3   8   3   8   3   3
'''
df.drop(['D','E'], inplace=True, axis=0)
print(df)
'''
   국어  수학  영어  과학  체육  사회  IT
C   6  26   6  26   6  26  26
'''
