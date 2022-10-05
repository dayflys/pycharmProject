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

print('1. DataFrame 행별(열을 축)최대 최소')
x = df.max(axis=1)
print(x,type(x))
'''
1. DataFrame 행별(열을 축)최대 최소
B    300.0
E    221.0
C     43.0
A     50.0
D     61.0
dtype: float64 <class 'pandas.core.series.Series'>
'''
x = df.min(axis=1)
print(x,type(x))
'''
B    4.0
E    5.0
C    6.0
A    4.0
D    1.0
dtype: float64 <class 'pandas.core.series.Series'>
'''
print('2. DataFrame 행별(열을 축) 누적최대 누적최소')
x = df.cummax(axis=1)
print(x)
'''
2. DataFrame 행별(열을 축) 누적최대 누적최소
     c     a      b
B  4.0  14.0  300.0
E  5.0  35.0  221.0
C  6.0  26.0   43.0
A  NaN   4.0   50.0
D  1.0  33.0   61.0
'''
x = df.cummin(axis=1)
print(x)
'''
     c    a    b
B  4.0  4.0  4.0
E  5.0  5.0  5.0
C  6.0  6.0  6.0
A  NaN  4.0  4.0
D  1.0  1.0  1.0
'''
print('3. DataFrame 행별(열을 축) 최대,최소값의 label 반환')
x = df.idxmax(axis=1)
print(x)
'''
3. DataFrame 행별(열을 축) 최대,최소값의 label 반환
B    b
E    b
C    b
A    b
D    b
'''
x = df.idxmin(axis=1)
print(x)
'''
B    c
E    c
C    c
A    a
D    c
dtype: object
'''
print('4. DataFrame 행별(열을 축) 합계 및 누적 합계')
x = df.sum(axis=1)
print(x)
'''
4. DataFrame 행별(열을 축) 합계 및 누적 합계
B    318.0
E    261.0
C     75.0
A     54.0
D     95.0
dtype: float64
'''
x = df.cumsum(axis=1)
print(x)
'''
     c     a      b
B  4.0  18.0  318.0
E  5.0  40.0  261.0
C  6.0  32.0   75.0
A  NaN   4.0   54.0
D  1.0  34.0   95.0
'''
print('5. DataFrame 행별(열을 축) 평균, 중앙값')
x = df.mean(axis=1)
print(x)
'''
5. DataFrame 행별(열을 축) 평균, 중앙값
B    106.000000
E     87.000000
C     25.000000
A     27.000000
D     31.666667
dtype: float64
'''
x = df.median(axis=1)
print(x)
'''
B    14.0
E    35.0
C    26.0
A    27.0
D    33.0
dtype: float64
'''
print('6. DataFrame 행별(열을 축) 곱 및 누적곱')
x = df.prod(axis=0)
print(x)
'''
6. DataFrame 행별(열을 축) 곱 및 누적곱
c    1.200000e+02
a    1.681680e+06
b    8.695245e+09
dtype: float64
'''
x = df.cumprod(axis=1)
print(x)
'''
     c      a        b
B  4.0   56.0  16800.0
E  5.0  175.0  38675.0
C  6.0  156.0   6708.0
A  NaN    4.0    200.0
D  1.0   33.0   2013.0
'''
print('7. DataFrame 행별(열을 축) 분산 및 표준편차')
x = df.var(axis=1)
print(x)
'''
7. DataFrame 행별(열을 축) 분산 및 표준편차
B    28252.000000
E    13692.000000
C      343.000000
A     1058.000000
D      901.333333
dtype: float64
'''
x = df.std(axis=1)
print(x)
'''
B    168.083313
E    117.012820
C     18.520259
A     32.526912
D     30.022214
dtype: float64
'''
print('6. DataFrame 행별(열을 축) 행개수 ')
x = df.count(axis=1) #nan은 빠진다.
print(x)
'''
6. DataFrame 행별(열을 축) 행개수 
B    3
E    3
C    3
A    2
D    3
dtype: int64
'''
