'''

    범용 함수 (universial function)

    1. 개념
        데이터의 요소별로 연산을 수행하는 함수 => 이로인해 벡터 연산이 가능하게 한다.

    이항함수 => 파라미터가 ndarray 두 개가 필요한 함수
'''

import numpy as np

arr = np.arange(5)
arr2 = arr+10
#1. np.add: 덧셈
print("1. 덧셈 출력:", np.add(arr,arr2)) #1. 덧셈 출력: [10 12 14 16 18]


#2. np.subtract: 뺄셈 출력
print("2. 뺄셈 출력:", np.subtract(arr2, arr)) #2. 뺄셈 출력: [10 10 10 10 10]

#3. np.multiply: 곱셈 출력
print("3. 곱셈 출력:", np.multiply(arr,arr2)) #3. 곱셈 출력: [ 0 11 24 39 56]

#4. np.divide: 나눗셈 출력
print("4. 나눗셈 출력:", np.divide(arr,arr2)) #4. 나눗셈 출력: [0.         0.09090909 0.16666667 0.23076923 0.28571429]

#5. np.floor_divide: 나눗셈 몫 출력
arr = np.array([5,6,7,8])
arr2 = np.array([3,3,3,3])
print("5. 나눗셈 몫 출력:", np.floor_divide(arr,arr2)) #5. 나눗셈 몫 출력: [1 2 2 2]

#6. np.mod, np.remainder : 나눗셈 나머지 출력
print("6. 나눗셈 나머지 출력:", np.mod(arr,arr2)) # 6. 나눗셈 나머지 출력: [2 0 1 2]
print("6. 나눗셈 나머지 출력:", np.remainder(arr,arr2)) #6. 나눗셈 나머지 출력: [2 0 1 2]

#7. np.maximum : 인덱스별 큰 값 반환
print("7. 인덱스별 큰 값 출력:", np.maximum(arr,arr2)) #7. 인덱스별 큰 값 출력: [5 6 7 8]

#8. np.minimum : 인덱스별 작은 값 출력
print("8. 인덱스별 작은 값 출력:", np.minimum(arr,arr2)) #8. 인덱스별 작은 값 출력: [3 3 3 3]

#9. np.greater : 값 비교하여 크면 True 반환, 아니면 False 반환
print("9. 값 비교후 boolean 값(크냐) 출력:", np.greater(arr,arr2)) #9. 값 비교후 boolean 값(크냐) 출력: [ True  True  True  True]
print("9. 값 비교후 boolean 값(크거나 같냐) 출력:", np.greater_equal(arr,arr2)) #9. 값 비교후 boolean 값(크거나 같냐) 출력: [ True  True  True  True]

#10. np.less : 값 비교하여 작으면 True 반환, 아니면 False 반환
print("10. 값 비교후 boolean 값(작냐) 출력:", np.less(arr,arr2)) #10. 값 비교후 boolean 값(작냐) 출력: [False False False False]
print("10. 값 비교후 boolean 값(작거나 같냐) 출력:", np.less_equal(arr,arr2)) #10. 값 비교후 boolean 값(작거나 같냐) 출력: [False False False False]
print("10. 값 비교후 boolean 값(같냐) 출력:", np.equal(arr,arr2)) #10. 값 비교후 boolean 값(같냐) 출력: [False False False False]
print("10. 값 비교후 boolean 값(같지 않냐) 출력:", np.not_equal(arr,arr2)) #10. 값 비교후 boolean 값(같지 않냐) 출력: [ True  True  True  True]

#11. np.power : 제곱 출력
arr = np.array([1,2,3])
arr2= arr + 5
print("11. 제곱 출력:", np.power(arr,arr2)) #11. 제곱 출력: [   1  128 6561]

