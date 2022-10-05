'''
    DataFrame에 컬럼 추가

    1.dict 방식

        df['새로운 컬럼'] = 리스트|series|(ndarray도 상관 없다)

        2. df.assign() 함수 이용

        new_df = df.assign(컬럼명=리스트)

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

df = df.assign(과학=[7,6,4,2,1]) #컬럼명에는 "" 처리를 진행하면 안된다.
print(df)
'''
   국어  수학  영어  과학
0   4  14  43   7
1   5  35  50   6
2   6  26  61   4
3   7   8   3   2
4   8   3  56   1
'''


df = df.assign(체육=[7,6,4,2,1],가정=[7,6,4,2,1])
print(df)
'''
   국어  수학  영어  과학  총합  체육  가정
0   4  14  43   7  61   7   7
1   5  35  50   6  90   6   6
2   6  26  61   4  93   4   4
3   7   8   3   2  18   2   2
4   8   3  56   1  67   1   1
'''
df = df.assign(총합=lambda df:df['국어']+df['수학']+df['영어']+df['체육']+df['가정']) #x에는 df가 전달된다.
print(df)
'''
   국어  수학  영어  과학  총합
0   4  14  43   7  61
1   5  35  50   6  90
2   6  26  61   4  93
3   7   8   3   2  18
4   8   3  56   1  67
'''
df = df.assign(평균=lambda df:df['총합']/5)
print(df)
'''
   국어  수학  영어  과학  체육  가정   총합    평균
0   4  14  43   7   7   7   75  15.0
1   5  35  50   6   6   6  102  20.4
2   6  26  61   4   4   4  101  20.2
3   7   8   3   2   2   2   22   4.4
4   8   3  56   1   1   1   69  13.8
'''
df = df.assign(합격여부= ['합격' if avg >20 else '불합격' for avg in df['평균']])
print(df)
'''
   국어  수학  영어  과학  체육  가정   총합    평균 합격여부
0   4  14  43   7   7   7   75  15.0  불합격
1   5  35  50   6   6   6  102  20.4   합격
2   6  26  61   4   4   4  101  20.2   합격
3   7   8   3   2   2   2   22   4.4  불합격
4   8   3  56   1   1   1   69  13.8  불합격
'''