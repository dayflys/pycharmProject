'''

    1. dict 이용
    -> column 이 키가 되고 , row 가 value가 된다
    => 기본적으로 원본 dict 순서로 보여진다.

    2. 원하는 컬럼 순서 변경
    df = pd.DataFrame({key:값,key:값}, columns= ['컬럼명','컬럼명','컬럼명'])

    3. 내용 보기

        1. 컬럼 정보
            df.columns
            df.keys()
        2. 인덱스 정보
             index
        3. 내용 정보


'''

import pandas as pd
import numpy as np

#1. dict 이용 => 컬럼별 데이터의 갯수가 동일해야한다.
dict_value =   {'c1': [4,5,6]
                ,'c2': [14,35,26]
                ,'c3': [43,50,61]}
print(dict_value.keys()) #dict_keys(['c1', 'c2', 'c3'])
df = pd.DataFrame(dict_value)

print("1. 컬럼 정보(컬럼 라벨 정보)")
print(df.columns,list(df.columns)) #Index(['c1', 'c2', 'c3'], dtype='object') ['c1', 'c2', 'c3']
#라벨이 필요하면 list 함수로 감싸준다.
print(df.keys(),list(df.keys())) #Index(['c1', 'c2', 'c3'], dtype='object') ['c1', 'c2', 'c3']

print("2. 인덱스 정보(행 라벨 정보)")
print(df.index) #RangeIndex(start=0, stop=3, step=1)

print("3. 내용보기")
'''
    df.values ==> values는 원래 함수
    
        @property 
        def values(...):
            pass
        
            
'''
print(df.values, type(df.values)) #<class 'numpy.ndarray'>
'''
3. 내용보기
[[ 4 14 43]
 [ 5 35 50]
 [ 6 26 61]]
'''
print(df.to_numpy(),type(df.to_numpy())) #<class 'numpy.ndarray'> => df.values와 같은 결과가 나오지만 더 권장 된다.
'''
[[ 4 14 43]
 [ 5 35 50]
 [ 6 26 61]]
 '''

