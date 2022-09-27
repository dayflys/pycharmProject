'''
    ndarray 삭제 (axis 개념 )
    -문법:
        new_arr = np.delete(arr, idx|fancy|slice, axis = None|0|1)
        -삭제된 새로운 ndarray를 반환한다.
        -삭제 옵션은 idx(값 하나), fancy(값 여러개), 슬라이싱 모두 가능
        예>
        -idx: 5
        -fancy: [0,2,4]
        -슬라이싱 :np.s_[1:3]

    ===> 기본적으로 위치값으로 삭제한다.
    ===> 순방향, 역방향 모두 가능
    ===> axis=None 이 기본 (대부분 다른 함수들의 axis의 기본값은 0)이다.
        axis 값을 지정하지 않으면 flat된다. => 1차원으로 변경

    ===> axis = None
        => flatten됨

    ===> axis = 0
        => 행이 삭제됨

    ===> axis = 1
        => 행이 삭제됨

    -슬라이싱도 가능함
'''

import numpy as np

arr = np.arange(25).reshape((5,5))
print(arr)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
'''
#가. axis = None (기본)
# 행* 열 값과 요소의 개수가 안맞으면 flatten 된다 (1차원 배열로 바뀐다. 이를 flatten 된다고 한다.)

#1. idx 삭제
new_arr = np.delete(arr, -1)
print(new_arr) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]


#2. fancy
new_arr = np.delete(arr, [0,-1])
print(new_arr) # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

#3. slice
new_arr = np.delete(arr, np.s_[:8])
print(new_arr) # [ 8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]


#나. axis = 0 ===> 행 삭제

#1. idx 삭제
new_arr = np.delete(arr, -1, axis=0) #가장 마지막 행 삭제
print(new_arr) #[[ 0  1  2  3  4] [ 5  6  7  8  9] [10 11 12 13 14] [15 16 17 18 19]]

#2. fancy
new_arr = np.delete(arr, [0,-1], axis=0) # 첫 번째와 가장 마지막 행 삭제
print(new_arr) # [[ 5  6  7  8  9] [10 11 12 13 14] [15 16 17 18 19]]

#3. slice
new_arr = np.delete(arr,np.s_[:3], axis=0) # 0~2행 까지 삭제
print(new_arr) # [[15 16 17 18 19] [20 21 22 23 24]]


#나. axis = 1 ===> 열 삭제

#1. idx 삭제
new_arr = np.delete(arr, -1, axis=1) #가장 마지막 열 삭제
print(new_arr) #[[ 0  1  2  3] [ 5  6  7  8] [10 11 12 13] [15 16 17 18] [20 21 22 23]]

#2. fancy
new_arr = np.delete(arr, [0,-1], axis=1) # 첫 번째와 가장 마지막 열 삭제
print(new_arr) #[[ 1  2  3] [ 6  7  8] [11 12 13] [16 17 18] [21 22 23]]

#3. slice
new_arr = np.delete(arr,np.s_[:3], axis=1) # 0~2열 까지 삭제
print(new_arr) #[[ 3  4] [ 8  9] [13 14] [18 19] [23 24]]