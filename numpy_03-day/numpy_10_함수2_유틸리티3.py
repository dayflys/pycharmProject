'''

    유틸리티 3
    1.   np.where(조건식) : 조건에 일치하는 인덱스 반환
         np.where(조건식, 참 , 거짓) : 3항 연산자 벡터화

    2. np.unique(arr): 중복제거 하고 정렬해서 반환


'''

import numpy as np

#1.np.where(조건식): 조건과 일치하는 인덱스 반환
arr = np.array([9,8,7,6,5,4,3])
print("5값의 위치:", np.where(arr==5)) #5값의 위치 (array([4]),)
new_arr = np.delete(arr,np.where(arr==5))
print("5값 삭제 :", new_arr) #5값 삭제 : [9 8 7 6 4 3]

#2.np.where(조건식, 참, 거짓): 3항 연산자 벡터화 버전
arr = np.array([19,87,58,6,5,4,3])
print(arr%2 == 0) #[False False  True  True False  True False]
print("짝수면 -1 홀수면 0:", np.where(arr%2 == 0, -1, 0)) #짝수면 -1 홀수면 0: [ 0  0 -1 -1  0 -1  0]

#3.np.unique(arr): 중복 제거 후 정렬해서 반환
arr = np.array([1,19,8,58,6,8,4,3,4,3])
print(arr) #[ 1 19  8 58  6  8  4  3  4  3]
print("np.unique : ", np.unique(arr)) #np.unique :  [ 1  3  4  6  8 19 58]
