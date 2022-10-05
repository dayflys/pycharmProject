'''
    filter 함수
    -> sql의 like 연산자와 비슷한 역할도 있다
    -> 문법
        => df.filter(items=리스트, axis=0|1)
        => df.filter(like:문자열, axis=0|1)
        => df.filter(regex = 정규표현식, axis= 0|1)
        https://wikidocs.net/4308
        ==> 주민번호, 이메일 등 다양한 사용자 입력값을 패턴으로 유효성 체크 및 검색 가능

'''

import pandas as pd
import numpy as np

dict_value =   {'c1': [4,5,6,7,8]
                ,'c2': [14,35,26,8,3]
                ,'d1': [43,50,61,3,56]
                ,'e2': [43,50,61,3,56]}
df  = pd.DataFrame(dict_value, index=['mouse','rabbit','habbit','hunt','mount'])
print(df)
'''
        c1  c2  d1  e2
mouse    4  14  43  43
rabbit   5  35  50  50
habbit   6  26  61  61
hunt     7   8   3   3
mount    8   3  56  56
'''
print("1. c1,d1 컬럼 조회")
print(df.filter(items=['c1','d1'], axis=1))
'''
        c1  d1
mouse    4  43
rabbit   5  50
habbit   6  61
hunt     7   3
mount    8  56
'''
print("2. mouse,hunt 컬럼 조회")
print(df.filter(items=['mouse','hunt'], axis=0))
'''
       c1  c2  d1  e2
mouse   4  14  43  43
hunt    7   8   3   3
'''
print("3. c가 들어간 컬럼 조회")
print(df.filter(like='c', axis=1))
'''
        c1  c2
mouse    4  14
rabbit   5  35
habbit   6  26
hunt     7   8
mount    8   3
'''
print("4. 2가 들어간 컬럼 조회")
print(df.filter(like='2', axis=1))
'''
4. 2가 들어간 컬럼 조회
        c2  e2
mouse   14  43
rabbit  35  50
habbit  26  61
hunt     8   3
mount    3  56
'''
print("5. bit가 들어간 컬럼 조회")
print(df.filter(like='bit', axis=0))
'''
5. bit가 들어간 컬럼 조회
        c1  c2  d1  e2
rabbit   5  35  50  50
habbit   6  26  61  61
'''

print("6. unt가 들어간 컬럼 조회")
print(df.filter(like='unt', axis=0))
'''
6. unt가 들어간 컬럼 조회
       c1  c2  d1  e2
hunt    7   8   3   3
mount   8   3  56  56
'''

dict_value =   {'aa.a': [4,5,6,7,8]
                ,'aa2': [14,35,26,8,3]
                ,'b.29': [43,50,61,3,56]
                ,'98ab': [43,50,61,3,56]}
df  = pd.DataFrame(dict_value, index=['mouse','rabbit','habbit','hunt','mount'])
print(df)
print("7. 컬럼중에서 .이 들어간 컬럼 조회")
print(df.filter(regex='\.')) #. 조회
'''
        aa.a  b.29
mouse      4    43
rabbit     5    50
habbit     6    61
hunt       7     3
mount      8    56
'''
print("8. 컬럼중에서 a로 시작하는 컬럼 조회")
print(df.filter(regex='^a')) #시작하는 문자 조회
'''
        aa.a  aa2
mouse      4   14
rabbit     5   35
habbit     6   26
hunt       7    8
mount      8    3
'''
print("8. 컬럼중에서 b로 끝나는 컬럼 조회")
print(df.filter(regex='b$')) #끝나는 것 조회
'''
        98ab
mouse     43
rabbit    50
habbit    61
hunt       3
mount     56
'''
print("8. 컬럼중에서 [1-9] 범위의 숫자로 끝나는 컬럼 조회")
print(df.filter(regex='[1-9]$')) #끝나는 것 조회
'''
        aa2  b.29
mouse    14    43
rabbit   35    50
habbit   26    61
hunt      8     3
mount     3    56
'''