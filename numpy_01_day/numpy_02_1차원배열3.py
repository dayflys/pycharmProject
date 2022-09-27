'''
    zeros,ones,empty,full => 전부 ndarray 타입으로 반환된다.
    -np.zeros(shape) => 모양에 맞게끔 0을 전부 채워준다. 기본 타입은 float64로 반환된다.
                    => dtype= np.int64 와 같은 방법으로 타입 변경 가능하다
    -np.ones(shape) => 모양에 맞게끔 1을 전부 채워준다. 기본 타입은 float64로 반환된다.
    -np.empty(shpae) => 모양에 맞게끔 임의의 값을 채워준다.
    -np.full(shape, value) => 모양에 맞게끔 value값으로 채워준다.
'''

import numpy as np

#1. np.zeros(shape)
print("1. np.zeros(shape)")
s = np.zeros(5) #zeros(shape, dtype=float, order='C', *, like=None)
print(s) #[0. 0. 0. 0. 0.]
s = np.zeros(5, dtype=np.int32) #dtype 의 크기를 주고싶다면 np.int32와 같이 np. 을 붙여준다.
print(s) #[0 0 0 0 0]
print('*'*100)

#2. np.ones(shape)
print("2. np.ones(shape)")
s = np.ones(5) #
print(s) #[1. 1. 1. 1. 1.]
s = np.ones(5, dtype=int)
s = np.ones(5, dtype=np.int32) #dtype 의 크기를 주고싶다면 np.int32와 같이 np. 을 붙여준다.
print(s) #[1 1 1 1 1]
print('*'*100)


#3. np.empty(shape)
print("3. np.empty(shape)")
s = np.empty(10)
print(s) #[0.         2.73861279 2.23606798 4.70372193 2.73861279 2.23606798 4.70372193 2.73861279 2.23606798 0.        ]
s = np.empty(10, dtype=int)
s = np.empty(10, dtype=np.int64) #dtype 의 크기를 주고싶다면 np.int32와 같이 np. 을 붙여준다.
print(s) #[                  0 4613349226564681734 4612217596255138984 4616981938510815294 4613349226564724111 4612217596255138984 4616981938510815294 4613349226564724111 4612217596255138984 0]
print('*'*100)

#4. np.full(shape,value)
print("4. np.full(shape,value)")
s = np.full(10,100) #100값 10개의 요소를 반환
print(s.dtype) #int64
print(s) #[100 100 100 100 100 100 100 100 100 100]
s = np.full(10, 100,dtype=int)
s = np.full(10, 100,dtype=np.int32) #dtype 의 크기를 주고싶다면 np.int32와 같이 np. 을 붙여준다.
print(s) #[100 100 100 100 100 100 100 100 100 100]
print('*'*100)