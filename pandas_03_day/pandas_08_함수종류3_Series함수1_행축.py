'''

    함수

    1. DataFrame의 함수
        -최대,최소 : df.max(), df.min()
        -누적 최대,최소 : df.cummax(), df.cummin()
        -최대,최소값의 label 반환: df.idxmax(),df.idxmin()
        -합계: df.sum()
        -평균:
    2. Series의 함수

'''

#df 함수
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

print('1. 특정 컬럼별(행을 축)최대 최소')
x = df['c'].max(axis=0)
print(x)
'''
1. 특정 컬럼별(행을 축)최대 최소
6.0
'''
x = df['c'].min(axis=0)
print(x) #1.0

print('2. 여러 특정 컬럼별(행을 축)최대 최소')
x = df[['c','a']].max(axis=0)
print(x)
'''
2. 여러 특정 컬럼별(행을 축)최대 최소
c     6.0
a    35.0
dtype: float64
'''
x = df[['c','a']].min(axis=0)
print(x)
'''
c    1.0
a    4.0
dtype: float64
'''

print('2. DataFrame 컬럼별(행을 축) 누적최대 누적최소')
x = df['c'].cummax(axis=0)
print(x)
'''
B    4.0
E    5.0
C    6.0
A    NaN
D    6.0
Name: c, dtype: float64
'''
x = df['c'].cummin(axis=0)
print(x)
'''
B    4.0
E    4.0
C    4.0
A    NaN
D    1.0
Name: c, dtype: float64
'''
print('3. DataFrame 컬럼별(행을 축) 최대,최소값의 label 반환')
x = df['c'].idxmax(axis=0)
print(x)
'''
3. DataFrame 컬럼별(행을 축) 최대,최소값의 label 반환
C
'''
x = df['c'].idxmin(axis=0)
print(x)
'''
D
'''
print('4. DataFrame 컬럼별(행을 축) 합계 및 누적 합계')
x = df['c'].sum(axis=0)
print(x)
'''
4. DataFrame 컬럼별(행을 축) 합계 및 누적 합계
16.0
'''
x = df['c'].cumsum(axis=0)
print(x)
'''
B     4.0
E     9.0
C    15.0
A     NaN
D    16.0
Name: c, dtype: float64
'''
print('5. DataFrame 컬럼별(행을 축) 평균, 중앙값')
x = df['c'].mean(axis=0)
print(x)
'''
5. DataFrame 컬럼별(행을 축) 평균, 중앙값
4.0
'''
x = df['c'].median(axis=0)
print(x)
'''
4.5
'''
print('6. DataFrame 컬럼별(행을 축) 곱 및 누적곱')
x = df['c'].prod(axis=0)
print(x)
'''
6. DataFrame 컬럼별(행을 축) 곱 및 누적곱
120.0
'''
x = df['c'].cumprod(axis=0)
print(x)
'''
B      4.0
E     20.0
C    120.0
A      NaN
D    120.0
Name: c, dtype: float64
'''
print('7. DataFrame 컬럼별(행을 축) 분산 및 표준편차')
x = df['c'].var(axis=0)
print(x)
'''
7. DataFrame 컬럼별(행을 축) 분산 및 표준편차
4.666666666666667
'''
x = df['c'].std(axis=0)
print(x)
'''
2.160246899469287
'''
print('6. DataFrame 컬럼별(행을 축) 행개수 ')
x = df['c'].count() #nan은 빠진다.
print(x)
'''
6. DataFrame 컬럼별(행을 축) 행개수 
4
'''
