'''
    zeros,ones,empty,full => 전부 ndarray 타입으로 반환된다.
    -np.zeros((행,열)) => 모양에 맞게끔 0을 전부 채워준다. 기본 타입은 float64로 반환된다.
                    => dtype= np.int64 와 같은 방법으로 타입 변경 가능하다
    -np.ones((행,열)) => 모양에 맞게끔 1을 전부 채워준다. 기본 타입은 float64로 반환된다.
    -np.empty((행,열)) => 모양에 맞게끔 임의의 값을 채워준다.
    -np.full((행,열), value) => 모양에 맞게끔 value값으로 채워준다.
'''

import numpy as np

#1. np.zeros((행,열))
print("1. np.zeros((행,열))")
s = np.zeros((2,3))
print(s) #[[0. 0. 0.][0. 0. 0.]]
s = np.zeros((2,3), dtype=np.int32)
print(s) #[[0 0 0][0 0 0]]
print('*'*100)

#2. np.ones((행,열))
print("2. np.ones((행,열))")
s = np.ones((2,3))
print(s) #[[1. 1. 1.] [1. 1. 1.]]
s = np.ones((2,3), dtype=int)
s = np.ones((2,3), dtype=np.int32)
print(s) #[[1 1 1] [1 1 1]]
print('*'*100)


#3. np.empty((행, 열))
print("3. np.empty((행, 열))")
s = np.empty((2,3))
print(s) #[[5.e-324 5.e-324 5.e-324] [5.e-324 5.e-324 5.e-324]]
s = np.empty((2,3), dtype=int)
s = np.empty((2,3), dtype=np.int64)
print(s) #[[1 1 1][1 1 1]]
print('*'*100)

#4. np.full((행, 열),value)
print("4. np.full((행, 열),value)")
s = np.full((2,3),100)
print(s.dtype)
print(s) #[[100 100 100] [100 100 100]]
s = np.full((2,3), 100,dtype=int)
s = np.full((2,3), 100,dtype=np.int32)
print(s) #[[100 100 100] [100 100 100]]
print('*'*100)

'''
    
    다차원 배열 이해하기
    
    (층, 행, 열)
    1. 열 해석하고 행 해석하고 층 해석하는 순서
    2. 열은 1차원의 요소길이
        행은 1차원의 길이
        층은 2차원이 길이
        
    예> (2,3,1) 의미?
    
    1. 열 값이 1이기 때문에 1차원의 길이가 1개 있음을 의미. 즉 [10]
    2. 행 값이 3이기 때문에 1차원인 [10]가 3개 있음을 의미. 즉 [[10][10][10]]
    3. 층 값이 2이기 때문에 2차원인 [[10][10][10]]가 2개 있음을 의미한다.
     즉, 
        [
        [[10][10][10]]
        [[10][10][10]]
        ]
'''