'''

    범용 함수 (universial function)

    1. 개념
        데이터의 요소별로 연산을 수행하는 함수 => 이로인해 벡터 연산이 가능하게 한다.

'''

#1. 범용 함수 확인 => 범용함수는 ufunc라는 문구가 뜬다
import numpy as np

print(np.abs) #<ufunc 'absolute'>

#2. 일반 함수 확인
print(np.array) #<built-in function array>