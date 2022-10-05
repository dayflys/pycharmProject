'''
    DataFrame에 행 추가

    1.한번에 하나씩 추가
        df.append(df2, ignore_index=True)

    2. 한번에 여러개 추가

        df.concat([df,df2,....], ignore_index=True)


'''

import pandas as pd
import numpy as np
dict_value =   {'국어': [4,5,6,7,8]
                ,'수학': [14,35,26,8,3]
                ,'영어': [43,50,61,3,56]}

df = pd.DataFrame(dict_value)
print(df)
'''
   국어  수학  영어
0   4  14  43
1   5  35  50
2   6  26  61
3   7   8   3
4   8   3  56
'''
dict_value2 =   {'국어': [100,98]
                ,'수학': [64,95]
                ,'영어': [73,100]}
df2 = pd.DataFrame(dict_value2)
print(df2)
'''
    국어  수학   영어
0  100  64   73
1   98  95  100
'''
dict_value3 =   {'국어': [1,8]
                ,'수학': [6,5]
                ,'영어': [3,10]}
df3 = pd.DataFrame(dict_value3)
print(df3)
'''
   국어  수학  영어
0   1   6   3
1   8   5  10
'''

new_df =pd.concat([df,df2,df3], ignore_index=True)
print(new_df)
'''
    국어  수학   영어
0    4  14   43
1    5  35   50
2    6  26   61
3    7   8    3
4    8   3   56
5  100  64   73
6   98  95  100
7    1   6    3
8    8   5   10
'''