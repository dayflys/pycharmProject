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

print('1. DataFrame 컬럼별(행을 축)최대 최소')
x = df.max(axis=0)
print(x,type(x))
'''
c      6.0
a     35.0
b    300.0
dtype: float64 <class 'pandas.core.series.Series'>
'''
x = df.min(axis=0)
print(x,type(x))
'''
c     1.0
a     4.0
b    43.0
dtype: float64 <class 'pandas.core.series.Series'>
'''
print('2. DataFrame 컬럼별(행을 축) 누적최대 누적최소')
x = df.cummax(axis=0)
print(x)
'''
     c   a    b
B  4.0  14  300
E  5.0  35  300
C  6.0  35  300
A  NaN  35  300
D  6.0  35  300
'''
x = df.cummin(axis=0)
print(x)
'''
     c   a    b
B  4.0  14  300
E  4.0  14  221
C  4.0  14   43
A  NaN   4   43
D  1.0   4   43
'''
print('3. DataFrame 컬럼별(행을 축) 최대,최소값의 label 반환')
x = df.idxmax(axis=0)
print(x)
'''
c    C
a    E
b    B
dtype: object
'''
x = df.idxmin(axis=0)
print(x)
'''
c    D
a    A
b    C
dtype: object
'''
print('4. DataFrame 컬럼별(행을 축) 합계 및 누적 합계')
x = df.sum(axis=0)
print(x)
'''
c     16.0
a    112.0
b    675.0
dtype: float64
'''
x = df.cumsum(axis=0)
print(x)
'''
      c    a    b
B   4.0   14  300
E   9.0   49  521
C  15.0   75  564
A   NaN   79  614
D  16.0  112  675
'''
print('5. DataFrame 컬럼별(행을 축) 평균, 중앙값')
x = df.mean(axis=0)
print(x)
'''
c      4.0
a     22.4
b    135.0
dtype: float64
'''
x = df.median(axis=0)
print(x)
'''
c     4.5
a    26.0
b    61.0
dtype: float64
'''
print('6. DataFrame 컬럼별(행을 축) 곱 및 누적곱')
x = df.prod(axis=0)
print(x)
'''
c    1.200000e+02
a    1.681680e+06
b    8.695245e+09
dtype: float64
'''
x = df.cumprod(axis=0)
print(x)
'''
       c        a           b
B    4.0       14         300
E   20.0      490       66300
C  120.0    12740     2850900
A    NaN    50960   142545000
D  120.0  1681680  8695245000
'''
print('7. DataFrame 컬럼별(행을 축) 분산 및 표준편차')
x = df.var(axis=0)
print(x)
'''
c        4.666667
a      173.300000
b    13946.500000
dtype: float64
'''
x = df.std(axis=0)
print(x)
'''
c      2.160247
a     13.164346
b    118.095300
dtype: float64
'''
print('6. DataFrame 컬럼별(행을 축) 행개수 ')
x = df.count(axis=0) #nan은 빠진다.
print(x)
'''
c    4
a    5
b    5
dtype: int64
'''
print('6. DataFrame 통합 통계 정보')
x = df.describe()
print(x)
'''
              c          a         b
count  4.000000   5.000000    5.0000
mean   4.000000  22.400000  135.0000
std    2.160247  13.164346  118.0953
min    1.000000   4.000000   43.0000
25%    3.250000  14.000000   50.0000
50%    4.500000  26.000000   61.0000
75%    5.250000  33.000000  221.0000
max    6.000000  35.000000  300.0000
'''
print('7. DataFrame에 대한  정보')
x = df.info()
print(x)
'''
Index: 5 entries, B to D
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   c       4 non-null      float64
 1   a       5 non-null      int64  
 2   b       5 non-null      int64  
dtypes: float64(1), int64(2)
memory usage: 160.0+ bytes
None
'''
print('10. 지정된 개수만큼만 상위 행 보기')
x = df.head(3) #기본값은 5개의 행
print(x)
'''
     c   a    b
B  4.0  14  300
E  5.0  35  221
C  6.0  26   43
'''
print('11. 지정된 개수만큼만 하위 행 보기')
x = df.tail(3) #기본값은 5개의 행
print(x)
'''
     c   a   b
C  6.0  26  43
A  NaN   4  50
D  1.0  33  61
'''