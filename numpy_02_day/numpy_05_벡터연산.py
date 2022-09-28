'''

    numpy의 벡터 연산(vectorized operation)
    - 기존 파이썬에서 지원 안되던 요소간의 연산이 가능하다.
    - 연산 성능도 매우 좋다
    - 연산의 종류
        => 비교연산, 산술연산 지원
    - 연산 대상
        => 다차원 배열, 스칼라

    * 브로드캐스팅(broadcasting)
    -서로 다른 차원을 가진 다차원 배열이 연산할 때, 연산이 가능하도록 차원을 맞추어 주는 작업을 의미한다.
'''

#1.python 연산
print("리스트와 스칼라 연산")
x = [1,2,3]
x2 = 5
print(x * x2) #[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print([1,2,3] * 5) #[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print("*"* 100)

print("리스트와 리스트 연산")
x = [1,2,3]
x2 = [10,20,30]
print(x + x2) #[1, 2, 3, 10, 20, 30]
print([1,2,3] + [10,20,30]) #[1, 2, 3, 10, 20, 30]
print("*"* 100)


#2.numpy 연산
import numpy as np
print("ndarray와 스칼라 연산") #자동으로 broadcasting이 되어 연산됨.
arr = np.array([1,2,3])
print(arr + 5) #[6 7 8]
print(arr - 5) #[-4 -3 -2]
print(arr * 5) #[ 5 10 15]
print(arr / 5) #[0.2 0.4 0.6]
print("*"* 100)

print("ndarray와 ndarray 연산")
arr1 = np.array([1,2,3])
arr2 = np.array([10,20,30])
#print(np.array([1,2,3]) + np.array([10,20,30])) # 반드시 shape 일치해야 한다.
print(arr1 + arr2) #[11 22 33]
print(arr1 - arr2) #[ -9 -18 -27]
print(arr1 * arr2) #[10 40 90]
print(arr1 / arr2) #[0.1 0.1 0.1]
print("*"* 100)

#비교 연산 가능 => 벡터 연산
arr = np.arange(10)
print(arr) #[0 1 2 3 4 5 6 7 8 9]
print("2의 배수냐? ", arr%2 == 0 ) #[ True False  True False  True False  True False  True False]
print("5보다 크냐? ", arr > 5 ) #[False False False False False False  True  True  True  True]
print("5보다 크고 짝수냐? ", (arr%2 == 0) & (arr >5) ) #[False False False False False False  True False  True False]
print("5보다 크거나 짝수냐? ", (arr%2 == 0) | (arr >5) ) #[ True False  True False  True False  True  True  True  True]
print("*"* 100)

#다차원 모두 벡터 연산이 가능하다. # 반드시 shape이 일치해야 한다.
arr = np.arange(9).reshape(3,3)
arr2 = np.arange(10,19).reshape(3,3)
x = [[1,2,3],[4,5,6],[7,8,9]]
print(arr+ arr2)
'''
[[10 12 14]
 [16 18 20]
 [22 24 26]]
'''
print(arr+ x, type(arr+ x))
'''
[[ 1  3  5]
 [ 7  9 11]
 [13 15 17]]
x가 ndarray로 형변환 되서 계산됨. <class 'numpy.ndarray'>
 '''
print(arr +10 )
'''
[[10 11 12]
 [13 14 15]
 [16 17 18]]
 10이 broadcasting되서 계산됨 
 '''