'''

    타입 변환하는 2가지 방법

    1. dtype 속성 이용

    2. astype 함수 이용

'''
import numpy as np

#1. int ---> float
arr1 = np.array([10,20,30])
arr2 = np.array([10,20,30], dtype=np.float64)
print(arr1, arr1.dtype) #[10 20 30] int64 (저장된 데이터를 보고 타입을 자동으로 설정)
print(arr2, arr2.dtype) #[10. 20. 30.] float64 (정수를 지정했으나 dtype에 의해서 float으로 변경됨)
print('*'* 100)

#2. float --> int
arr = np.array([1.34,2.5,3.8])
arr2 = np.array([1.34,2.5,3.8], dtype=np.int64)
print(arr, arr.dtype) #[1.34 2.5  3.8 ] float64
print(arr2, arr2.dtype) #[1 2 3] int64 => (실수를 지정했으나 dtype에 의해서 int로 변경됨) 정수형으로 바뀌면 소수점이 절삭된다. 소수점 값이 있어도 절삭된다.

#3. int ----> 문자열 ( bytes, 유니코드 ) #numpy에서는 string이라는 자료형은 존재하지 않는다.
arr = np.array([10,20,30])
arr2 = np.array([10,20,30], dtype=np.string_) #숫자를 bytes 타입으로 바꿀 때는 np.string_ 으로 바꾼다.
arr3 = np.array([10,20,30], dtype=np.str_) # 숫자를 유니코드 타입으로 바꿀 때는 np.str_ 으로 바꾼다.
print(arr2, arr2.dtype) #[b'10' b'20' b'30'] |S2
print(arr3, arr3.dtype) #['10' '20' '30'] <U2
print('*'*100)
#4. 문자열 ----> 정수 #문자열의 기본은 유니코드이다.
arr = np.array(['10','20','30'])
arr2 = np.array(['10','20','30'], dtype=np.int32)
arr3 = np.array(['10','20','30'], dtype=np.float64)
print(arr2, arr2.dtype) #[10 20 30] int32
print(arr3, arr3.dtype) #[10. 20. 30.] float64

