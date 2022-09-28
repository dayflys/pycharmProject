'''
    축
    => 행 : axis =0 , 열: axis = 1 , 층 : axis = 2

    열병합 ==>
    1. np.hstack(튜플) ==> 수평(horizental)방향으로 병합
    2. np.concatenate(튜플, axis =1 ) ==> axis = 1 인 컬럼방향으로 병합
    3. np.column_stack(튜플) ==> 컬럼방향으로 병합

'''
import numpy as np

arr = np.arange(9).reshape(3,3)
print(arr)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
 '''
arr2 = arr+100
print(arr2)
'''
[[100 101 102]
 [103 104 105]
 [106 107 108]]
'''

#가. np.hstack(튜플)
arr3 = np.hstack((arr,arr2))
print(arr3)
'''
[[  0   1   2 100 101 102]
 [  3   4   5 103 104 105]
 [  6   7   8 106 107 108]]
 '''
#나. np.concatenate(튜플, axis = 1)
arr3 = np.concatenate((arr,arr2), axis=1)
print(arr3)
'''
[[  0   1   2 100 101 102]
 [  3   4   5 103 104 105]
 [  6   7   8 106 107 108]]
 '''
#다. np.column_stack(튜플)
arr3 = np.column_stack((arr,arr2))
print(arr3)
'''
[[  0   1   2 100 101 102]
 [  3   4   5 103 104 105]
 [  6   7   8 106 107 108]]
 '''