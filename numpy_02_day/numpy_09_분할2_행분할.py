'''
    축
    => 행 : axis =0 , 열: axis = 1 , 층 : axis = 2

    열병합 ==>
    1. np.vsplit
    2. np.split( axis = 0)


'''
import numpy as np

arr = np.arange(12).reshape(4,3)
print(arr)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
 '''

arr1, arr2 = np.vsplit(arr,2)
print(arr1)
'''
[[0 1 2]
 [3 4 5]]
'''
print(arr2)
'''
[[ 6  7  8]
 [ 9 10 11]]
'''
arr1, arr2 = np.split(arr,2,axis=0)
print(arr1)
'''
[[0 1 2]
 [3 4 5]]
'''
print(arr2)
'''
[[ 6  7  8]
 [ 9 10 11]]
'''