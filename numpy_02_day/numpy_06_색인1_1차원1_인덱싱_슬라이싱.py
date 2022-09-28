'''

    1차원 배열(벡터) 색인
    1) 인덱싱, 슬라이싱 (기존 파이썬 문법과 동일)
        -기본적으로 위치값을 이용
        -순방향
        -역방향


'''

# 1. 인덱싱
import numpy as np
arr = np.array(['A','B','C','D','E','F'])
print(arr[0]) # A 순방향
print(arr[-1]) # F 역방향

#2. 슬라이싱
arr = np.array(['A','B','C','D','E','F'])
print(arr[0:4]) # ['A' 'B' 'C' 'D'] 순방향
print(arr[-5:-1]) # ['B' 'C' 'D' 'E'] 역방향
print(arr[4:]) # ['E' 'F']
print(arr[:6]) # ['A' 'B' 'C' 'D' 'E' 'F']
print(arr[:6:2]) # ['A' 'C' 'E']

print(arr[::-1]) #['F' 'E' 'D' 'C' 'B' 'A'] #역순
print(arr[:]) #['A' 'B' 'C' 'D' 'E' 'F']
print(arr[...]) #['A' 'B' 'C' 'D' 'E' 'F'] # ... = all 과 같다.

#차원 변경
print(arr)
print(arr[..., np.newaxis]) #차원을 바꿀때 np.newaxis를 활용한다. 앞에 오면 1행으로 된 2차원을 , 뒤에 오면 1열로 된 2차원을 반환한다.
'''
[['A']
 ['B']
 ['C']
 ['D']
 ['E']
 ['F']]
 '''
print(arr[np.newaxis,...]) #[['A' 'B' 'C' 'D' 'E' 'F']]

