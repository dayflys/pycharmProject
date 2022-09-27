'''
    arange([start,] stop[,step])
    -> 기본적으로 1차원만 지정이 가능하다.
    => 따라서, shape을 통해 2차원 변경 작업이 필요하다.
    가.
        => arr.reshape=(행, 열)
        => arr.reshape=(-1, 열)
        => arr.reshape=(행, -1)
    나. reshape((행, 열)) 함수 이용
'''

import numpy as np

#1. arr.shape = (행, 열) 이용하여 2차원으로 변경
print("1. np.arange(stop)")
x = np.arange(10)
x.shape = (2,5)
print(x) #[[0 1 2 3 4][5 6 7 8 9]]


#2. reshape((행, 열)| 행, ) 함수 이용하여 2차원으로 변경
x = np.arange(10).reshape((5,2)) #[[0 1 2 3 4] [5 6 7 8 9]]