'''

    범용 함수 (universial function)

    1. 개념
        데이터의 요소별로 연산을 수행하는 함수 => 이로인해 벡터 연산이 가능하게 한다.

    단항함수 => 파라미터가 ndarray 한 개가 필요한 함수
'''

import numpy as np

arr = np.array([-4.62,-2.19,0,1.57,3.40,4.06])

#1. np.abs: 절댓값
print("1. 절댓값 출력:", np.abs(arr)) #1. 절댓값 출력: [4.62 2.19 0.   1.57 3.4  4.06]

#2. np.around: 0.5를 기준으로 올림 혹은 내림
print("2. 0.5 기준으로 올림 혹은 내림 출력:", np.around(arr)) #2. 0.5 기준으로 올림 혹은 내림 출력: [-5. -2.  0.  2.  3.  4.]

#3. np.round: 소수점 n자리에서 반올림
arr = np.array([-4.6298775,-2.19788,0,1.5786654,3.409876,4.06066])
print("3. 반올림 출력:", np.round(arr)) #3. 반올림 출력: [-5. -2.  0.  2.  3.  4.] => 소수점 자리수를 안주면 정수 출력
print("3. 반올림 출력:", np.round(arr,1)) #3. 반올림 출력: [-4.6 -2.2  0.   1.6  3.4  4.1]
print("3. 반올림 출력:", np.round(arr,2)) #3. 반올림 출력: [-4.63 -2.2   0.    1.58  3.41  4.06]

#4. np.rint: 가우스 출력
arr = np.array([-4.62,-2.19,0,1.57,3.40,4.06])
print("4. 가우스 출력:", np.rint(arr)) #4. 가우스 출력: [-5. -2.  0.  2.  3.  4.]

#5. np.fix: 0 방향으로 가장 가까운 정수로 올림 또는 내림
arr = np.array([-4.62,-2.19,0,1.57,3.40,4.06])
print("5. 0 방향으로 가장 가까운 정수를 출력:", np.fix(arr)) #5. 0 방향으로 가장 가까운 정수를 출력: [-4. -2.  0.  1.  3.  4.]

#6. np.ceil : 각 원소보다 같거나 큰 정수값으로 올림
arr = np.array([-4.62,-2.19,0,1.57,3.40,4.06])
print("6. 정수 값으로 올림 출력:", np.ceil(arr)) #6. 정수 값으로 올림 출력: [-4. -2.  0.  2.  4.  5.]

#7. np.floor : 각 원소보다 같거나 작은 정수값으로 올림
arr = np.array([-4.62,-2.19,0,1.57,3.40,4.06])
print("7. 정수값으로 내림 출력:", np.floor(arr)) #7. 정수값으로 내림 출력: [-5. -3.  0.  1.  3.  4.]

#8. np.trunc : 소수점 부분 절삭
arr = np.array([-4.62,-2.19,0,1.57,3.40,4.06])
print("8. 소수점 부분 절삭 출력:", np.trunc(arr)) #8. 소수점 부분 절삭 출력: [-4. -2.  0.  1.  3.  4.]

#9. np.sqrt : 제곱근
arr = np.array([4,9,16])
print("9. 제곱근 출력:", np.sqrt(arr)) #9. 제곱근 출력: [2. 3. 4.] => float64 형으로 출력됨



