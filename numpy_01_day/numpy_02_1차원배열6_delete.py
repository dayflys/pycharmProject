'''
    ndarray 삭제
    -문법:
        new_arr = np.delete(arr, idx|fancy|slice, axis = 0)
        -삭제된 새로운 ndarray를 반환한다.
        -삭제 옵션은 idx(값 하나), fancy(값 여러개), 슬라이싱 모두 가능
        예>
        -idx: 5
        -fancy: [0,2,4]
        -슬라이싱 :np.s_[1:3]

    ===> 기본적으로 위치값으로 삭제한다.
    ===> 순방향, 역방향 모두 가능

    -슬라이싱도 가능함
'''

import numpy as np
# in-place 속성이 아닌, return a new array이므로 복제하여 삭제한다.
# obj 파라미터에는 idx|fancy|slice 가 가능하다.

arr = np.array([9,8,7,6,5,4,3])
new_arr = np.delete(arr,0) #인덱싱
new_arr1 = np.delete(arr,[0,3,5]) #fancy
new_arr2 = np.delete(arr,[-1,-2,-3]) #fancy 역방향
new_arr3 = np.delete(arr,np.s_[0:5]) #slicing
new_arr4 = np.delete(arr,np.s_[:3]) #slicing start만
new_arr5 = np.delete(arr,np.s_[3:]) #slicing end만

print(new_arr,arr)#[8 7 6 5 4 3] [9 8 7 6 5 4 3]
print(new_arr1,arr)#[8 7 5 3] [9 8 7 6 5 4 3]
print(new_arr2,arr)#[9 8 7 6] [9 8 7 6 5 4 3]
print(new_arr3,arr)#[4 3] [9 8 7 6 5 4 3]
print(new_arr4,arr)#[6 5 4 3] [9 8 7 6 5 4 3]
print(new_arr5,arr)#[9 8 7] [9 8 7 6 5 4 3]