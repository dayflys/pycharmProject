'''
    python에서 문자열 처리
    예> sss = 'helllo'
        sss.함수

    numpy에서 문자열 처리
    => np.char.함수
    예> x = np.array(["AAA","BBB"])
        np.char.capitalize(x)

    pandas 에서 문자열 처리
    ==> df['컬럼'].str.함수


'''

import numpy as np
import pandas as pd

df = pd.DataFrame({'name':['Hong', 'park','KIM'],
                   'age': [20,42,56],
                   'address':['seoul','pUsAn','JeJU']})
print(df)
'''
   name  age address
0  Hong   20   seoul
1  park   42   pUsAn
2   KIM   56    JeJU
'''
print('1. replace')
xxx = df['name'].str.replace('Hong','HONG')
print(xxx)
'''
1. replace
0    HONG
1    park
2     KIM
Name: name, dtype: object ==> 변경된 것만 반환해준다.
'''
df['name'] = df['name'].str.replace('Hong','HONG')
print(df)
'''
   name  age address
0  HONG   20   seoul
1  park   42   pUsAn
2   KIM   56    JeJU ==> 원본에 적용하기 위해서는 변경된 시리즈에 다시 할당 해주면 된다.
'''
print('2. contains')
xxx = df['name'].str.contains('park')
print(xxx)
'''
0    False
1     True
2    False
Name: name, dtype: bool
'''
xxx = df['name'].str.contains('park|KIM') #park 또는 KIM
print(xxx)
'''
0    False
1     True
2     True
Name: name, dtype: bool
'''
print('3. 원-핫 인코딩 방법')
'''
원-핫 인코딩이란?
-> 문자열을 숫자로 표현하는 방법
    1.라벨 인코딩
    ['Hong','park','KIM'] ==> [0,1,2]
    ==> 마킹한 용도의 숫자를 머신러닝은 학습을 하기 때문에 크다, 작다로 인식해 등수를 지정할려고 노력한다.
    2.원-핫 인코딩
    ==> ['Hong','park','KIM'] ==> [1 0 0] Hong
                                  [0 1 0] park
                                  [0 0 1] KIM
    
'''
xxx = df['name'].str.get_dummies()
print(xxx)
'''
   HONG  KIM  park
0     1    0     0
1     0    0     1
2     0    1     0
'''