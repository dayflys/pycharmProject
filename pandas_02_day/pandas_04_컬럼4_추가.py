'''
    DataFrame에 컬럼 추가

    1.dict 방식

        df['새로운 컬럼'] = 리스트|series|(ndarray도 상관 없다)

        2. df.assign() 함수 이용

        new_df = df.assign(컬럼명=리스트)

        3. df 와 df2 연

        pd.concat()

'''

import pandas as pd
import numpy as np
dict_value =   {'국어': [4,5,6,7,8]
                ,'수학': [14,35,26,8,3]}

df = pd.DataFrame(dict_value)

dict_value2 = {'영어': [43,50,61,3,56]}

df2 = pd.DataFrame(dict_value2)

# print(df,df2)
'''
   국어  수학
0   4  14
1   5  35
2   6  26
3   7   8
4   8   3

    영어
0  43
1  50
2  61
3   3
4  56
'''

new_df = pd.concat([df,df2],axis=1)
print(new_df)
'''
   국어  수학  영어
0   4  14  43
1   5  35  50
2   6  26  61
3   7   8   3
4   8   3  56
'''
new_df = pd.concat([df2,df],axis=1)
print(new_df)
'''
   영어  국어  수학
0  43   4  14
1  50   5  35
2  61   6  26
3   3   7   8
4  56   8   3
'''

##################
