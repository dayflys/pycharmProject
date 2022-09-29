'''
    유틸리티 함수 => 일종의 범용함수라고 보면 되며, 앞 서 정리한 범용 함수보다 axis 개념이 더 들어가 있다.
    -> axis 이용해서 행별 또는 열별로 연산

    1.  np.prod: 곱계산
        np.nanprod: nan 값을 1로 바꿔서 곱 처리
        np.cumprod: 누적 곱하기


    2.  np.sum: 합계산
        np.nansum: nan 값을 0로 바꿔서 합 처리
        np.cumsum: 누적 더하기

'''

import numpy as np

print('1. np.prod: 곱계산 - 1차원')
arr1D = np.array([1,2,3,4])
print(arr1D) #[1 2 3 4]
print(np.prod(arr1D)) #1*2*3*4 = 24

arr2D = np.array([[1,2],[3,4],[5,6]])
print(arr2D)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print('2. np.prod: 곱계산 - 2차원')

print(np.prod(arr2D, axis=0)) # [15 48] 행방향 위*아래 => input이 행방향으로 들어간다고 생각하자
print(np.prod(arr2D, axis=1)) # [ 2 12 30] 열방향 왼쪽*오른쪽 => input이 열방향으로 들어간다고 생각하자

print('3. np.nanprod: 곱계산 - 2차원')
arr2D = np.array([[1,2],[3,4],[5,np.nan]]) # np.nan : 파이썬의 None 과 비슷하다 full name= Not a Number
print(arr2D)
'''
[[ 1.  2.]
 [ 3.  4.]
 [ 5. nan]]
'''
print(np.prod(arr2D, axis=0)) #[15. nan] => nan 과 연산시 값은 nan 출력
print(np.prod(arr2D, axis=1)) # [ 2. 12. nan] => nan 과 연산시 값은 nan 출력

print(np.nanprod(arr2D, axis=0)) #[15.  8.] => nan을 1로 처리해서 연산
print(np.nanprod(arr2D, axis=1)) # [ 2. 12.  5.] => nan을 1로 처리해서 연산



print('4. np.cumprod: 누적 곱계산 - 2차원')
arr2D = np.array([[1,2],[3,4],[5,6]])
print(np.cumprod(arr2D, axis=0)) # [[1,2],[1*3,2*4],[1*3*5,2*4*6]]
print(np.cumprod(arr2D, axis=1)) # [[1,1*2],[3,3*4],[5,5*6]]

print("*"* 100)

print('1. np.sum: 합계산 - 1차원')
arr1D = np.array([1,2,3,4])
print(arr1D) #[1 2 3 4]
print(np.sum(arr1D)) #10

arr2D = np.array([[1,2],[3,4],[5,6]])
print(arr2D)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print('2. np.sum: 합계산 - 2차원')

print(np.sum(arr2D, axis=0)) # [ 9 12] 행방향 위+아래 => input이 행방향으로 들어간다고 생각하자
print(np.sum(arr2D, axis=1)) # [ 3  7 11] 열방향 왼쪽+오른쪽 => input이 열방향으로 들어간다고 생각하자

print('3. np.nansum: 합계산 - 2차원')
arr2D = np.array([[1,2],[3,4],[5,np.nan]]) # np.nan : 파이썬의 None 과 비슷하다 full name= Not a Number
print(arr2D)
'''
[[ 1.  2.]
 [ 3.  4.]
 [ 5. nan]]
'''
print(np.sum(arr2D, axis=0)) #[ 9. nan] => nan 과 연산시 값은 nan 출력
print(np.sum(arr2D, axis=1)) # [ 3.  7. nan] => nan 과 연산시 값은 nan 출력

print(np.nansum(arr2D, axis=0)) #[9. 6.] => nan을 0으로 처리해서 연산
print(np.nansum(arr2D, axis=1)) # [3. 7. 5.] => nan을 0으로 처리해서 연산



print('4. np.cumsum: 누적 합계산 - 2차원')
arr2D = np.array([[1,2],[3,4],[5,6]])
print(np.cumsum(arr2D, axis=0)) #[[ 1  2][ 4  6][ 9 12]]
print(np.cumsum(arr2D, axis=1)) #[[ 1  3][ 3  7][ 5 11]]
