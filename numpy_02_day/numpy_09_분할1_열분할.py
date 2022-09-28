'''
    축
    => 행 : axis =0 , 열: axis = 1 , 층 : axis = 2

    열분할 ==> 분할 개수가 동일해야 한다.
    1. hsplit(튜플)
    2. split(axis =1)

'''
import numpy as np

arr = np.arange(12).reshape(3,4)
print(arr)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
 '''

arr2,arr3 = np.hsplit(arr,2)
print(arr2,arr3)
'''
arr2:
[[0 1]
 [4 5]
 [8 9]] 
 arr3:
 [[ 2  3]
 [ 6  7]
 [10 11]]
'''


arr2,arr3 = np.split(arr,2, axis=1)
print(arr2,arr3)
'''
arr2:
[[0 1]
 [4 5]
 [8 9]] 
 arr3:
 [[ 2  3]
 [ 6  7]
 [10 11]]
 '''