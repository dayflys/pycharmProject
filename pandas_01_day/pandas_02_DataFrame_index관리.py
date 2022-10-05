'''

    DataFrame의 인덱스 관리

    1. 인덱스 관리

        가. 새로운 값으로 index로 설정할 때
            df.index=[값, 값2,...]

        나. 기존 컬럼 값으로 index로 설정 할때
            df.set_index('기존컬럼명', drop=True, inplace=False)

'''

import numpy as np
import pandas as pd

dict_value ={ 'date': ['2002','2003'],
              'name': ['홍길동','이순신'],
              'age': [20,30]}

df = pd.DataFrame(dict_value)
print(df)
'''
   date name  age
0  2002  홍길동   20
1  2003  이순신   30
'''

#1. 기존 컬럼 값으로 index로 설정할 때
# df.set_index()
new_df = df.set_index("date")
print(new_df)
'''
     name  age
date          
2002  홍길동   20
2003  이순신   30
'''
print(df)
'''
   date name  age ==> append = False => True로 변경되면 기존 index에 추가된다.
0  2002  홍길동   20 => drop =True : 기존 컬럼을 제거하고 인덱스로 설정 
1  2003  이순신   30 ==> inplace 값이 false이기 때문에 복사본을 생성한다. (자신이 수정되지 않고 복사본을 생성해서 반환)
'''
new_df = df.set_index("date", drop= False)
print(new_df)
'''
      date name  age
date                
2002  2002  홍길동   20
2003  2003  이순신   30 => 인덱스 값으로 이동했던 date 데이터를 drop=False 이기 때문에 기존 컬럼을 제거하지 않고 출력함 
'''
new_df = df.set_index("date", append=True) #append=False (기존 인덱스를 새로운 값으로 덮어쓰기)
#append =True (기존 인덱스에 새로운 값을 추가 한다)
print(new_df)
'''
      name  age
  date          
0 2002  홍길동   20
1 2003  이순신   30
'''

df.set_index("date", inplace=True)
print(df)
'''
     name  age
date          
2002  홍길동   20
2003  이순신   30 ==> inplace=True 이기 때문에 원본이 수정되어 출력된다.
'''

dict_value ={ 'date': ['2002','2003'],
              'name': ['홍길동','이순신'],
              'age': [20,30]}
df = pd.DataFrame(dict_value)
new_df = df.set_index("date", append=True) #append=False (기존 인덱스를 새로운 값으로 덮어쓰기)
#append =True (기존 인덱스에 새로운 값을 추가 한다)
print(new_df)
print(new_df.index) #다중 index 경우 sql의 pk 다중 컬럼 지정 처럼 다중 index가 지정 된다.
# none 과 date 는 인덱스의 이름으로 지정 된다.
'''
MultiIndex([(0, '2002'),
            (1, '2003')],
           names=[None, 'date'])
'''