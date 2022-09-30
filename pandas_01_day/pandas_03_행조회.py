import pandas as pd
'''
    DataFrame 조회

    1. 컬럼 조회 -projection
        -sql: select 컬럼명 , 컬럼명2 ,....
        -df:
            df.컬럼명 ===> series 반환
            df['컬럼명'] ===> series로 반환
            df[ ['컬럼명','컬럼명2','컬럼명3',...] ] ===> 다중 컬럼 조회 가능, DataFrame으로 반환

    2. 행 조회 ==> sql의 selection = where절에서 조건식 지정

        가. 행 인덱스 라벨 이용

            df.loc[행 라벨] ===> 인덱싱 색인
            df.loc[[행 라벨,행 라벨,...]] ===> fancy 색인
            df.loc[start 행 라벨:stop 행 라벨] ===> 슬라이싱 색인, stop 행라벨 까지 포함된다
            df.loc[[True,False,...]] ===> boolean 색인
            
        나. 행 인덱스 위치 이용

            df.iloc[행 위치] ===> 인덱싱 색인
            df.iloc[[행 위치,행 위치,...]] ===> fancy 색인
            df.iloc[start 행 위치:stop 행 위치] ===> 슬라이싱 색인, stop 행 위치는 포함 안된다.
            => 위치로 찾을 때는 역방향이 가능하다.
            df.iloc[[True,False,...]] ===> boolean 색인
'''
import numpy as np

dict_value =   {'c1': [4,5,6,76]
                ,'c2': [14,35,26,8]
                ,'c3': [43,50,61,9]}
df  = pd.DataFrame(dict_value, index=list('ABCD'))
print(df)
'''
   c1  c2  c3
0 A   4  14  43
1 B   5  35  50 => ABCD는 라벨, loc 사용 
2 C   6  26  61 => 보이지 않는 인덱스, iloc 사용
3 D  76   8   9
'''

print('1. 행라벨로 조회')

print('가. 단일행 ')
print(df.loc['A']) #Series 반환
'''
c1     4
c2    14
c3    43
Name: A, dtype: int64
'''
print(df.loc['D']) #Series 반환
'''
c1    76
c2     8
c3     9
Name: D, dtype: int64
'''
print('나. 다중행 - fancy 색인 ')
print(df.loc[['A','C','D']]) #DataFrame 반환
'''
   c1  c2  c3
A   4  14  43
C   6  26  61
D  76   8   9
'''
print('다. 다중행 - 슬라이싱 ')
print(df.loc['B':'D']) #DataFrame 반환
'''
   c1  c2  c3
A   4  14  43
C   6  26  61
D  76   8   9
'''
print('라. 다중행 - boolean 색인 ')
print(df.loc[[True,False,False,False]]) #DataFrame 반환
'''
라. 다중행 - boolean 색인 
   c1  c2  c3
A   4  14  43
'''
print('2. 행 위치로 조회 (순방향/역방향 둘 다 조회 가능 )')
print('가. 단일행 ')
print(df.iloc[0]) #Series 반환
'''
c1     4
c2    14
c3    43
Name: A, dtype: int64
'''
print(df.iloc[-1]) #Series 반환, 역방향 가능
'''
c1    76
c2     8
c3     9
Name: D, dtype: int64
'''
print(df.iloc[2]) #Series 반환
'''
c1     6
c2    26
c3    61
Name: C, dtype: int64
'''
print('나. 다중행-fancy 색인 ')
print(df.iloc[[0,2,3]]) #DataFrame 반환,역방향 가능
'''
   c1  c2  c3
A   4  14  43
C   6  26  61
D  76   8   9
'''
print(df.iloc[[0,2,3,-1]]) #DataFrame 반환,역방향 가능
'''
   c1  c2  c3
A   4  14  43
C   6  26  61
D  76   8   9
D  76   8   9
'''
print('다. 다중행- 슬라이싱 ')
print(df.iloc[0:2]) #DataFrame 반환, 역방향 가능
'''
   c1  c2  c3
A   4  14  43
B   5  35  50
'''
print(df.iloc[0:-1]) #DataFrame 반환, 역방향 가능
'''
   c1  c2  c3
A   4  14  43
B   5  35  50
C   6  26  61
'''
print('라. 다중행-boolean 색인 ')
print(df.iloc[[True,False,True,False]]) #DataFrame 반환
'''
   c1  c2  c3
A   4  14  43
C   6  26  61
'''