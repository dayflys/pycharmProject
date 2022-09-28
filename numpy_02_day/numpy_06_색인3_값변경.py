'''

    색인을 활용한 값 변경

    1. 인덱싱 이용한 데이터 변경
'''

# 1.
import numpy as np

arr = np.arange(10)
print(arr) #[0 1 2 3 4 5 6 7 8 9]

#1. 인덱싱을 이용한 데이터 변경
arr[0] = 100
print(arr) #[100   1   2   3   4   5   6   7   8   9]
print('*'*100)

#2. 슬라이싱 이용한 데이터 변경
#가. 파이썬
x = list(range(9))
print(x) #[0, 1, 2, 3, 4, 5, 6, 7, 8]
# x[:3] = [100] #broadcasting 불가
x[:3] = [100,100,100] #shape 일치하면 일반 파이썬도 슬라이싱 데이터 변경 가능
print(x) #[100, 100, 100, 3, 4, 5, 6, 7, 8]
print('*'*100)

#나. numpy 슬라이싱 값 변경
arr = np.arange(10)
print(arr) #[0 1 2 3 4 5 6 7 8 9]
arr[:3] = 100
print(arr) #[100 100 100   3   4   5   6   7   8   9]

#3. fancy 색인 이용한 데이터 변경
arr = np.arange(10)
print(arr)
arr[[0,2,4]] = 100
print(arr) # [100   1 100   3 100   5   6   7   8   9]

#모든 값 변경
arr[:] = 999
arr[...] = 999
print(arr) #[999 999 999 999 999 999 999 999 999 999]

#4. boolean 색인 이용한 데이터 변경
arr = np.arange(10)
print(arr)
arr[arr%2 == 0] = 100
print(arr) # [100   1 100   3 100   5 100   7 100   9]
