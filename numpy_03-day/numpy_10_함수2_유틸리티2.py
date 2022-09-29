'''
    유틸리티 함수 => 일종의 범용함수라고 보면 되며, 앞 서 정리한 범용 함수보다 axis 개념이 더 들어가 있다.
    -> axis 이용해서 행별 또는 열별로 연산

    1.  np.prod: 곱계산
        np.nanprod: nan 값을 1로 바꿔서 곱 처리
        np.cumprod: 누적 곱하기
    2.  np.sum: 합계산
        np.nansum: nan 값을 0로 바꿔서 합 처리
        np.cumsum: 누적 더하기
    3. np.diff : 차분(n+1 에서 n 값을 뺀 것)
    4. np.mean : 평균
    5. np.median : 중앙값
    6. np.var : 분산(variance)
        => 평균을 기준으로 얼마나 데이터가 떨어져 있냐를 알려주는 지표
        => 공식 = (값 - 평균)^2/ 데이터 개수
            => 차이의 제곱의 평균
        => 차이값을 제곱했기 때문에 실제 체감할 수 있는 값으로는 부적합함
    7. np.std : 표준 편차
             ==> 분산을 제곱근 한 값이다. 뻥튀기된 분산값을 원위치
'''

import numpy as np

print('1. np.diff: 차분계산 - 1차원')
arr1D = np.array([1,2,4,8,15])
print(arr1D) #[1 2 3 4]
print(np.diff(arr1D)) #[1 2 4 7],1차 차분 => 차분은 요소의 개수가 n+1개면 요소가 n개인 ndarray를 출력한다
# n 값을 조절하면 n차 차분까지 진행한다.
print(np.diff(arr1D,n=2)) #[1 2 3], 2차 차분

arr2D = np.array([[1,2,4,8],[10,15,5,9]])
print(arr2D)
'''
[[ 1  2  4  8]
 [10 15  5  9]]
'''
print('2. np.diff: 차분계산 - 2차원')
print(np.diff(arr2D)) #diff 의 default는 axis 값중 가장 큰 값으로 차분 한다.
print(np.diff(arr2D, axis=0)) #[[ 9 13  1  1]]
print(np.diff(arr2D, axis=1)) #[[  1   2   4][  5 -10   4]]

print('3. np.mean: 평균계산 - 1차원')
arr1D = np.array([1,2,4,8,15])
print(arr1D) #[1 2 3 4]
print(np.mean(arr1D)) #6.0 => 평균을 출력하는 함수


print('4. np.mean: 평균계산 - 2차원')
arr2D = np.array([[1,2,4,8],[10,15,5,9]])
print(np.mean(arr2D)) #6.75 => mean 함수는 axis 가 지정되지 않으면 전 요소의 평균을 반환한다.
print(np.mean(arr2D, axis=0)) #[5.5 8.5 4.5 8.5]
print(np.mean(arr2D, axis=1)) #[3.75 9.75]


print('5. np.median: 중앙값 - 1차원')
arr1D = np.array([4,2,8,56,9])
print(arr1D) #[ 4  2  8 56  9]
print(np.median(arr1D)) #8.0 => 요소중 오름차순으로 정렬 후 중간 값을 출력하는 함수

arr1D = np.array([4,2,8,56,9,10])
print(arr1D) #[ 4  2  8 56  9 10]
print(np.median(arr1D)) #8.5 => 만약 요소가 짝수라면 오름차순으로 정렬 후 중간 두개의 값의 평균을 출력한다.

print('6. np.median: 중앙값 - 2차원')
arr2D = np.array([[1,2,4,8],[10,15,5,9]])
print(np.median(arr2D)) #median => median 함수는 axis 가 지정되지 않으면 전 요소의 중앙값을 반환한다.
print(np.median(arr2D, axis=0)) #[5.5 8.5 4.5 8.5]
print(np.median(arr2D, axis=1)) #[3.  9.5]

print('7. np.var: 분산 - 1차원')
arr1D = np.array([1,2,4,8,15])
print(arr1D) #[ 1  2  4  8 15]
print(np.var(arr1D)) #26.0
#####################
mean = np.mean(arr1D)
value = (1-mean)**2+(2-mean)**2+(4-mean)**2+(8-mean)**2+(15-mean)**2
print(value/5) #26.0
#####################
print('8. np.var: 분산 - 2차원')
arr2D = np.array([[1,2,4,8],[10,15,5,9]])
print(np.var(arr2D)) #18.9375 => var 함수는 axis 가 지정되지 않으면 전 요소 기준 분산을 반환한다.
print(np.var(arr2D, axis=0)) #[20.25 42.25  0.25  0.25]
print(np.var(arr2D, axis=1)) #[ 7.1875 12.6875]


print('9. np.std: 표준 편차 - 1차원')
arr1D = np.array([1,2,4,8,15])
print(arr1D) #[ 1  2  4  8 15]
print(np.std(arr1D)) #5.0990195135927845

print('10. np.std: 표준 편차 - 2차원')
arr2D = np.array([[1,2,4,8],[10,15,5,9]])
print(np.std(arr2D)) #4.351723796382303 => std 함수는 axis 가 지정되지 않으면 전 요소 기준 분산을 반환한다.
print(np.std(arr2D, axis=0)) #[4.5 6.5 0.5 0.5]
print(np.std(arr2D, axis=1)) #[2.68095132 3.56195171]